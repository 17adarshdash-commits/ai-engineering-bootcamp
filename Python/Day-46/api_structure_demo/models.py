"""
models.py - Pydantic request/response models for the item API.
"""

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Item name")
    price: float = Field(..., gt=0, description="Price, must be greater than 0")
    quantity: int = Field(default=0, ge=0, description="Quantity in stock, must be >= 0")


class ItemCreate(ItemBase):
    """Fields required to create a new item - id is assigned by the service."""

    pass


class Item(ItemBase):
    """Full item as returned by the API, including its assigned id."""

    id: int
