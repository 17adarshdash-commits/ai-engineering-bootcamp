"""
library_manager.py

Defines LibraryManager - validates input and performs every book/member/
borrowing operation against the books, members, and borrowed_books tables,
using a Database instance for every connection. All SQL here uses '?'
placeholders.
"""

import sqlite3

from book import Book
from member import Member

MIN_COPIES = 0


class LibraryError(Exception):
    """Base exception for all library-related errors."""


# -- Book errors --------------------------------------------------------
class DuplicateBookIDError(LibraryError):
    """Raised when a book ID already exists."""


class InvalidTitleError(LibraryError):
    """Raised when a book title is empty/blank."""


class InvalidAuthorError(LibraryError):
    """Raised when a book author is empty/blank."""


class InvalidCategoryError(LibraryError):
    """Raised when a book category is empty/blank."""


class InvalidCopiesError(LibraryError):
    """Raised when available copies is not a non-negative integer."""


class BookNotFoundError(LibraryError):
    """Raised when a book ID cannot be found."""


class BookHasActiveRecordsError(LibraryError):
    """Raised when deleting a book that still has borrow records referencing it."""


# -- Member errors -------------------------------------------------------
class DuplicateMemberIDError(LibraryError):
    """Raised when a member ID already exists."""


class InvalidNameError(LibraryError):
    """Raised when a member name is empty/blank."""


class InvalidEmailError(LibraryError):
    """Raised when an email fails basic validation."""


class DuplicateEmailError(LibraryError):
    """Raised when an email is already used by another member."""


class MemberNotFoundError(LibraryError):
    """Raised when a member ID cannot be found."""


class MemberHasActiveRecordsError(LibraryError):
    """Raised when deleting a member that still has borrow records referencing them."""


# -- Borrowing errors ------------------------------------------------------
class BookUnavailableError(LibraryError):
    """Raised when a book has no available copies left to borrow."""


class BorrowRecordNotFoundError(LibraryError):
    """Raised when an active (unreturned) borrow record cannot be found."""


class LibraryManager:
    """Performs validated operations on books, members, and borrowed_books."""

    def __init__(self, database):
        self.database = database

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_non_empty(value, error_cls, field_name):
        if not value or not value.strip():
            raise error_cls(f"{field_name} cannot be empty.")

    @staticmethod
    def _validate_copies(copies):
        try:
            copies = int(copies)
        except (TypeError, ValueError):
            raise InvalidCopiesError("Available copies must be an integer.")
        if copies < MIN_COPIES:
            raise InvalidCopiesError("Available copies cannot be negative.")
        return copies

    @staticmethod
    def _validate_email(email):
        if not email or "@" not in email or "." not in email.split("@")[-1]:
            raise InvalidEmailError(f"'{email}' is not a valid email address.")

    # ------------------------------------------------------------------
    # Books - Create
    # ------------------------------------------------------------------
    def add_book(self, book_id, title, author, category, available_copies):
        """Add a new book after validating all fields."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("SELECT 1 FROM books WHERE book_id = ?", (book_id,))
            if cursor.fetchone() is not None:
                raise DuplicateBookIDError(f"Book ID '{book_id}' already exists.")

            self._validate_non_empty(title, InvalidTitleError, "Title")
            self._validate_non_empty(author, InvalidAuthorError, "Author")
            self._validate_non_empty(category, InvalidCategoryError, "Category")
            available_copies = self._validate_copies(available_copies)

            book = Book(
                book_id=book_id,
                title=title.strip(),
                author=author.strip(),
                category=category.strip(),
                available_copies=available_copies,
            )
            conn.execute(
                "INSERT INTO books (book_id, title, author, category, available_copies) "
                "VALUES (?, ?, ?, ?, ?)",
                book.to_row(),
            )
            conn.commit()
            return book
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Books - Read
    # ------------------------------------------------------------------
    def get_book(self, book_id):
        """Fetch a single book by id, or raise BookNotFoundError."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT book_id, title, author, category, available_copies "
                "FROM books WHERE book_id = ?",
                (book_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise BookNotFoundError(f"Book ID '{book_id}' not found.")
            return Book.from_row(row)
        finally:
            conn.close()

    def display_books(self):
        """Return every book, ordered by title."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT book_id, title, author, category, available_copies "
                "FROM books ORDER BY title"
            )
            return [Book.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    def search_book(self, keyword):
        """Search books by ID, title, author, or category (case-insensitive substring match)."""
        conn = self.database.connect()
        try:
            pattern = f"%{keyword}%"
            cursor = conn.execute(
                """
                SELECT book_id, title, author, category, available_copies FROM books
                WHERE book_id LIKE ? OR title LIKE ? OR author LIKE ? OR category LIKE ?
                ORDER BY title
                """,
                (pattern, pattern, pattern, pattern),
            )
            return [Book.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Books - Update
    # ------------------------------------------------------------------
    def update_book(self, book_id, **updates):
        """Update one or more fields of an existing book."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("SELECT 1 FROM books WHERE book_id = ?", (book_id,))
            if cursor.fetchone() is None:
                raise BookNotFoundError(f"Book ID '{book_id}' not found.")

            fields = {}
            if "title" in updates:
                self._validate_non_empty(updates["title"], InvalidTitleError, "Title")
                fields["title"] = updates["title"].strip()
            if "author" in updates:
                self._validate_non_empty(updates["author"], InvalidAuthorError, "Author")
                fields["author"] = updates["author"].strip()
            if "category" in updates:
                self._validate_non_empty(updates["category"], InvalidCategoryError, "Category")
                fields["category"] = updates["category"].strip()
            if "available_copies" in updates:
                fields["available_copies"] = self._validate_copies(updates["available_copies"])

            if not fields:
                return self.get_book(book_id)

            set_clause = ", ".join(f"{column} = ?" for column in fields)
            values = list(fields.values()) + [book_id]
            conn.execute(f"UPDATE books SET {set_clause} WHERE book_id = ?", values)
            conn.commit()
            return self.get_book(book_id)
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Books - Delete
    # ------------------------------------------------------------------
    def delete_book(self, book_id):
        """Delete a book by id, refusing if borrow records still reference it."""
        conn = self.database.connect()
        try:
            try:
                cursor = conn.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
                conn.commit()
            except sqlite3.IntegrityError:
                raise BookHasActiveRecordsError(
                    f"Book ID '{book_id}' has borrow records and cannot be deleted."
                )
            if cursor.rowcount == 0:
                raise BookNotFoundError(f"Book ID '{book_id}' not found.")
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Members - Create
    # ------------------------------------------------------------------
    def add_member(self, member_id, name, email):
        """Add a new member after validating all fields."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("SELECT 1 FROM members WHERE member_id = ?", (member_id,))
            if cursor.fetchone() is not None:
                raise DuplicateMemberIDError(f"Member ID '{member_id}' already exists.")

            self._validate_non_empty(name, InvalidNameError, "Name")
            self._validate_email(email)

            cursor = conn.execute("SELECT 1 FROM members WHERE email = ?", (email,))
            if cursor.fetchone() is not None:
                raise DuplicateEmailError(f"Email '{email}' is already registered.")

            member = Member(member_id=member_id, name=name.strip(), email=email.strip())
            conn.execute(
                "INSERT INTO members (member_id, name, email) VALUES (?, ?, ?)",
                member.to_row(),
            )
            conn.commit()
            return member
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Members - Read
    # ------------------------------------------------------------------
    def get_member(self, member_id):
        """Fetch a single member by id, or raise MemberNotFoundError."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT member_id, name, email FROM members WHERE member_id = ?",
                (member_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise MemberNotFoundError(f"Member ID '{member_id}' not found.")
            return Member.from_row(row)
        finally:
            conn.close()

    def display_members(self):
        """Return every member, ordered by name."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT member_id, name, email FROM members ORDER BY name"
            )
            return [Member.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Members - Update
    # ------------------------------------------------------------------
    def update_member(self, member_id, **updates):
        """Update one or more fields of an existing member."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("SELECT 1 FROM members WHERE member_id = ?", (member_id,))
            if cursor.fetchone() is None:
                raise MemberNotFoundError(f"Member ID '{member_id}' not found.")

            fields = {}
            if "name" in updates:
                self._validate_non_empty(updates["name"], InvalidNameError, "Name")
                fields["name"] = updates["name"].strip()
            if "email" in updates:
                self._validate_email(updates["email"])
                cursor = conn.execute(
                    "SELECT 1 FROM members WHERE email = ? AND member_id != ?",
                    (updates["email"], member_id),
                )
                if cursor.fetchone() is not None:
                    raise DuplicateEmailError(f"Email '{updates['email']}' is already registered.")
                fields["email"] = updates["email"].strip()

            if not fields:
                return self.get_member(member_id)

            set_clause = ", ".join(f"{column} = ?" for column in fields)
            values = list(fields.values()) + [member_id]
            conn.execute(f"UPDATE members SET {set_clause} WHERE member_id = ?", values)
            conn.commit()
            return self.get_member(member_id)
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Members - Delete
    # ------------------------------------------------------------------
    def delete_member(self, member_id):
        """Delete a member by id, refusing if borrow records still reference them."""
        conn = self.database.connect()
        try:
            try:
                cursor = conn.execute(
                    "DELETE FROM members WHERE member_id = ?", (member_id,)
                )
                conn.commit()
            except sqlite3.IntegrityError:
                raise MemberHasActiveRecordsError(
                    f"Member ID '{member_id}' has borrow records and cannot be deleted."
                )
            if cursor.rowcount == 0:
                raise MemberNotFoundError(f"Member ID '{member_id}' not found.")
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Borrowing
    # ------------------------------------------------------------------
    def borrow_book(self, member_id, book_id):
        """Borrow a book for a member: validates both foreign keys and availability."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("SELECT 1 FROM members WHERE member_id = ?", (member_id,))
            if cursor.fetchone() is None:
                raise MemberNotFoundError(f"Member ID '{member_id}' not found.")

            cursor = conn.execute(
                "SELECT available_copies FROM books WHERE book_id = ?", (book_id,)
            )
            row = cursor.fetchone()
            if row is None:
                raise BookNotFoundError(f"Book ID '{book_id}' not found.")
            if row[0] <= 0:
                raise BookUnavailableError(f"Book ID '{book_id}' has no available copies.")

            conn.execute(
                "INSERT INTO borrowed_books (member_id, book_id, borrow_date, return_date) "
                "VALUES (?, ?, CURRENT_DATE, NULL)",
                (member_id, book_id),
            )
            conn.execute(
                "UPDATE books SET available_copies = available_copies - 1 WHERE book_id = ?",
                (book_id,),
            )
            conn.commit()
        finally:
            conn.close()

    def return_book(self, member_id, book_id):
        """Return a book: closes the oldest active borrow record and restocks the book."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                """
                SELECT borrow_id FROM borrowed_books
                WHERE member_id = ? AND book_id = ? AND return_date IS NULL
                ORDER BY borrow_date ASC
                LIMIT 1
                """,
                (member_id, book_id),
            )
            row = cursor.fetchone()
            if row is None:
                raise BorrowRecordNotFoundError(
                    f"No active borrow record for member '{member_id}' and book '{book_id}'."
                )
            borrow_id = row[0]

            conn.execute(
                "UPDATE borrowed_books SET return_date = CURRENT_DATE WHERE borrow_id = ?",
                (borrow_id,),
            )
            conn.execute(
                "UPDATE books SET available_copies = available_copies + 1 WHERE book_id = ?",
                (book_id,),
            )
            conn.commit()
        finally:
            conn.close()

    def show_borrowed_books(self):
        """Return every borrow record still active (not yet returned), joined with names/titles."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                """
                SELECT borrowed_books.borrow_id, members.name, books.title,
                       borrowed_books.borrow_date
                FROM borrowed_books
                INNER JOIN members ON borrowed_books.member_id = members.member_id
                INNER JOIN books ON borrowed_books.book_id = books.book_id
                WHERE borrowed_books.return_date IS NULL
                ORDER BY borrowed_books.borrow_date
                """
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def show_books_borrowed_by_member(self, member_id):
        """Return every borrow record (active and returned) for a single member, via LEFT JOIN."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("SELECT 1 FROM members WHERE member_id = ?", (member_id,))
            if cursor.fetchone() is None:
                raise MemberNotFoundError(f"Member ID '{member_id}' not found.")

            cursor = conn.execute(
                """
                SELECT books.title, borrowed_books.borrow_date, borrowed_books.return_date
                FROM members
                LEFT JOIN borrowed_books ON members.member_id = borrowed_books.member_id
                LEFT JOIN books ON borrowed_books.book_id = books.book_id
                WHERE members.member_id = ?
                ORDER BY borrowed_books.borrow_date
                """,
                (member_id,),
            )
            return cursor.fetchall()
        finally:
            conn.close()
