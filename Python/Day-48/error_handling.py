"""
error_handling.py - HTTPException, status codes, meaningful messages.

A small in-memory book store used purely to demonstrate the two shapes of
error a route reports: the resource simply doesn't exist (404) versus the
request itself is malformed (400). Successful paths return 200/201 as
usual; nothing here is about the data model - it's about what happens
when the request can't be satisfied.

Run with:
    uvicorn error_handling:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Error Handling Demo",
    description="HTTPException usage: existing vs. missing resources.",
    version="1.0.0",
)


class Book(BaseModel):
    id: int
    title: str
    author: str


books: list[Book] = [
    Book(id=1, title="Dune", author="Frank Herbert"),
    Book(id=2, title="Foundation", author="Isaac Asimov"),
]


def find_book(book_id: int) -> Book | None:
    return next((book for book in books if book.id == book_id), None)


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    """Return a book by id. 404 if no book has that id."""
    book = find_book(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
    return book


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> Book:
    """Create a book. 400 if the id is already taken or the title is blank."""
    if find_book(book.id) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Book with id {book.id} already exists",
        )
    if not book.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book title must not be empty",
        )
    books.append(book)
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    """Delete a book by id. 404 if no book has that id."""
    book = find_book(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
    books.remove(book)
