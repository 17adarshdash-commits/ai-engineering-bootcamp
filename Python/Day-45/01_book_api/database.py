"""
database.py - SQLite connection setup for the Book Management API.

Keeps all database-connection concerns (path, connection factory, schema
creation) in one place, separate from the CRUD logic and the API routes.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "books.db"


def get_connection() -> sqlite3.Connection:
    """Return a new SQLite connection with row access by column name."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Create the books table if it doesn't already exist."""
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
            """
        )
        conn.commit()
