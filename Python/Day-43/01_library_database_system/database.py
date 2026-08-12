"""
database.py

Owns the SQLite connection and schema for the library database system -
creating the database file/tables (with foreign keys enabled) if needed,
and providing a single place that opens/closes connections so no other
module talks to sqlite3 directly.
"""

import sqlite3

DB_FILE = "library.db"

CREATE_BOOKS_SQL = """
CREATE TABLE IF NOT EXISTS books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    available_copies INTEGER NOT NULL CHECK (available_copies >= 0)
)
"""

CREATE_MEMBERS_SQL = """
CREATE TABLE IF NOT EXISTS members (
    member_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
"""

CREATE_BORROWED_BOOKS_SQL = """
CREATE TABLE IF NOT EXISTS borrowed_books (
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id TEXT NOT NULL,
    book_id TEXT NOT NULL,
    borrow_date TEXT NOT NULL DEFAULT CURRENT_DATE,
    return_date TEXT,
    FOREIGN KEY (member_id) REFERENCES members (member_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id)
)
"""


class Database:
    """Manages the SQLite connection for the library's tables."""

    def __init__(self, db_file=DB_FILE):
        self.db_file = db_file
        self._init_schema()

    def _init_schema(self):
        """Create the database file (if needed) and every table (if needed)."""
        conn = self.connect()
        conn.execute(CREATE_BOOKS_SQL)
        conn.execute(CREATE_MEMBERS_SQL)
        conn.execute(CREATE_BORROWED_BOOKS_SQL)
        conn.commit()
        conn.close()

    def connect(self):
        """Open a fresh connection to the database file with foreign keys enforced."""
        conn = sqlite3.connect(self.db_file)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
