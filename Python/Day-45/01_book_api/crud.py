"""
crud.py - Database access layer for books.

All SQL lives here, kept separate from the API routes in main.py. Every query
is parameterized (using `?` placeholders) to avoid SQL injection.
"""

from typing import List, Optional

from database import get_connection
from models import Book, BookCreate, BookUpdate


def _row_to_book(row) -> Book:
    return Book(
        id=row["id"],
        title=row["title"],
        author=row["author"],
        category=row["category"],
        price=row["price"],
        stock=row["stock"],
    )


def get_all_books() -> List[Book]:
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM books ORDER BY id").fetchall()
        return [_row_to_book(row) for row in rows]


def get_book(book_id: int) -> Optional[Book]:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM books WHERE id = ?", (book_id,)
        ).fetchone()
        return _row_to_book(row) if row else None


def book_exists(book_id: int) -> bool:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT 1 FROM books WHERE id = ?", (book_id,)
        ).fetchone()
        return row is not None


def create_book(book: BookCreate) -> Book:
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO books (id, title, author, category, price, stock)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (book.id, book.title, book.author, book.category, book.price, book.stock),
        )
        conn.commit()
    return Book(**book.model_dump())


def update_book(book_id: int, book: BookUpdate) -> Optional[Book]:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            UPDATE books
            SET title = ?, author = ?, category = ?, price = ?, stock = ?
            WHERE id = ?
            """,
            (book.title, book.author, book.category, book.price, book.stock, book_id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            return None
    return Book(id=book_id, **book.model_dump())


def delete_book(book_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        return cursor.rowcount > 0
