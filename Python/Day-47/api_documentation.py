"""
api_documentation.py - A small GET/POST API to inspect automatic docs.

Run with:
    uvicorn api_documentation:app --reload

Docs:
    http://127.0.0.1:8000/docs   (Swagger UI - interactive, "Try it out")
    http://127.0.0.1:8000/redoc  (ReDoc - read-only reference view)
    http://127.0.0.1:8000/openapi.json  (the raw schema both are built from)

No complicated logic here - the point is to see how the route summary
(from each docstring), the request body schema (from Item), and the
response schema (from response_model=Item) all show up automatically in
both doc pages without writing any doc-specific code.
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(
    title="API Documentation Demo",
    description="A minimal API for exploring Swagger UI and ReDoc.",
    version="1.0.0",
)


class Item(BaseModel):
    id: int
    name: str
    price: float


items: list[Item] = []


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
    """Return every item currently stored."""
    return items


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item) -> Item:
    """Add a new item and return it."""
    items.append(item)
    return item
