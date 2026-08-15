"""
services.py - Business logic for items, kept separate from the routes.

Uses a simple in-memory store to keep the demo focused on project structure
(main/routers/models/services) rather than persistence - see 01_student_api
for a SQLite-backed example.
"""

from typing import Dict, List, Optional

from models import Item, ItemCreate

_items: Dict[int, Item] = {}
_next_id = 1


def list_items() -> List[Item]:
    return list(_items.values())


def get_item(item_id: int) -> Optional[Item]:
    return _items.get(item_id)


def create_item(item: ItemCreate) -> Item:
    global _next_id
    new_item = Item(id=_next_id, **item.model_dump())
    _items[_next_id] = new_item
    _next_id += 1
    return new_item


def delete_item(item_id: int) -> bool:
    return _items.pop(item_id, None) is not None
