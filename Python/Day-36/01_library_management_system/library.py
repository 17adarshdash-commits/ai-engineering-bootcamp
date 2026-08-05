import json

from book import Book
from exceptions import (
    BookAlreadyAvailableError,
    BookNotFoundError,
    BookUnavailableError,
    DuplicateBookIDError,
)


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, available=True):
        if book_id in self.books:
            raise DuplicateBookIDError(f"Book ID '{book_id}' already exists.")
        self.books[book_id] = Book(book_id, title, author, available)
        return self.books[book_id]

    def update_book(self, book_id, title=None, author=None, available=None):
        book = self._get_book(book_id)
        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if available is not None:
            book.available = available
        return book

    def delete_book(self, book_id):
        self._get_book(book_id)
        del self.books[book_id]

    def search_book(self, keyword):
        keyword = keyword.lower()
        return [
            book
            for book in self.books.values()
            if keyword in book.title.lower() or keyword in book.author.lower()
        ]

    def borrow_book(self, book_id):
        book = self._get_book(book_id)
        if not book.available:
            raise BookUnavailableError(f"Book ID '{book_id}' is already borrowed.")
        book.available = False
        return book

    def return_book(self, book_id):
        book = self._get_book(book_id)
        if book.available:
            raise BookAlreadyAvailableError(f"Book ID '{book_id}' is already available.")
        book.available = True
        return book

    def display_books(self):
        for book in self.books.values():
            print(book)

    def save_json(self, filepath):
        with open(filepath, "w") as f:
            json.dump([book.to_dict() for book in self.books.values()], f, indent=2)

    def load_json(self, filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
        self.books = {item["book_id"]: Book.from_dict(item) for item in data}

    def _get_book(self, book_id):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID '{book_id}' not found.")
        return self.books[book_id]
