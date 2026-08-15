"""
routers.py - API route definitions for items.

Handlers stay thin: parse input, delegate to services.py, translate the
result into an HTTP response with the right status code.
"""

from typing import List

from fastapi import APIRouter, HTTPException, status

import services
from models import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=List[Item])
def list_items() -> List[Item]:
    """Return all items."""
    return services.list_items()


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    """Retrieve a single item by ID."""
    item = services.get_item(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return item


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate) -> Item:
    """Create a new item."""
    return services.create_item(item)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    """Delete an item. 404 if it doesn't exist."""
    deleted = services.delete_item(item_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
