"""
crud_api_demo.py - Full CRUD (GET/POST/PUT/DELETE) over SQLite.

Combines the two prior demos: items live in SQLite (sqlite_fastapi_demo),
and every failure path raises a proper HTTPException with a meaningful
message (error_handling). This is the shape 01_task_manager_api scales
up into a modular project.

Run with:
    uvicorn crud_api_demo:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

DB_PATH = Path(__file__).parent / "items.db"

app = FastAPI(
    title="CRUD API Demo",
    description="Full CRUD for items, backed by SQLite.",
    version="1.0.0",
)


class ItemCreate(BaseModel):
    """Shape required to create/update an item. id is assigned by SQLite."""

    name: str
    price: float


class Item(ItemCreate):
    """Shape returned to clients - adds the database-assigned id."""

    id: int


def get_connection() -> sqlite3.Connection:
    """Open a short-lived connection with dict-like row access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the items table if it doesn't exist yet."""
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.get("/items", response_model=list[Item])
def get_items() -> list[Item]:
    """Return every item."""
    conn = get_connection()
    rows = conn.execute("SELECT id, name, price FROM items").fetchall()
    conn.close()
    return [Item(**dict(row)) for row in rows]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    """Return one item by id. 404 if it doesn't exist."""
    conn = get_connection()
    row = conn.execute(
        "SELECT id, name, price FROM items WHERE id = ?", (item_id,)
    ).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return Item(**dict(row))


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate) -> Item:
    """Insert a new item and return it with its assigned id."""
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO items (name, price) VALUES (?, ?)",
        (item.name, item.price),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return Item(id=new_id, name=item.name, price=item.price)


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate) -> Item:
    """Overwrite an existing item. 404 if it doesn't exist."""
    conn = get_connection()
    cursor = conn.execute(
        "UPDATE items SET name = ?, price = ? WHERE id = ?",
        (item.name, item.price, item_id),
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    if updated == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return Item(id=item_id, name=item.name, price=item.price)


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    """Delete an item by id. 404 if it doesn't exist."""
    conn = get_connection()
    cursor = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
