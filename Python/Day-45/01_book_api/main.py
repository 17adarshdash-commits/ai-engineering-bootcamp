"""
main.py - Book Management REST API.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from typing import List

from fastapi import FastAPI, HTTPException, status

import crud
from database import init_db
from models import Book, BookCreate, BookUpdate

app = FastAPI(
    title="Book Management API",
    description="A simple REST API for managing a book inventory, backed by SQLite.",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/books", response_model=List[Book])
def list_books() -> List[Book]:
    """Return all books."""
    return crud.get_all_books()


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    """Retrieve a single book by ID."""
    book = crud.get_book(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
    return book


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate) -> Book:
    """Create a new book. Business rules (beyond Pydantic's field validation):

    - id must not already exist (409 Conflict)
    """
    if crud.book_exists(book.id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Book with id {book.id} already exists",
        )
    return crud.create_book(book)


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate) -> Book:
    """Update an existing book. 404 if the book doesn't exist."""
    updated = crud.update_book(book_id, book)
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
    return updated


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    """Delete a book. 404 if the book doesn't exist."""
    deleted = crud.delete_book(book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
