"""
book.py

Defines the Book dataclass - a single book with an ID, title, author,
category, and available copy count, plus conversion to/from a plain tuple
so it can be (de)serialized to/from a SQLite row.
"""

from dataclasses import dataclass


@dataclass
class Book:
    """Represents a single book."""

    book_id: str
    title: str
    author: str
    category: str
    available_copies: int

    def to_row(self):
        """Convert the Book instance into a tuple matching the books table's column order."""
        return (self.book_id, self.title, self.author, self.category, self.available_copies)

    @classmethod
    def from_row(cls, row):
        """Build a Book instance from a SQLite row (book_id, title, author, category, available_copies)."""
        book_id, title, author, category, available_copies = row
        return cls(
            book_id=book_id,
            title=title,
            author=author,
            category=category,
            available_copies=available_copies,
        )

    def __str__(self):
        return (
            f"ID: {self.book_id} | {self.title} by {self.author} | "
            f"Category: {self.category} | Available: {self.available_copies}"
        )
