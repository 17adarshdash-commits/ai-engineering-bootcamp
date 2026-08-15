"""
database.py - SQLite connection setup for the Student Management API.

Keeps all database-connection concerns (path, connection factory, schema
creation) in one place, separate from CRUD logic, API routes, and schemas.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "students.db"


def get_connection() -> sqlite3.Connection:
    """Return a new SQLite connection with row access by column name."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Create the students table if it doesn't already exist."""
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT NOT NULL,
                cgpa REAL NOT NULL
            )
            """
        )
        conn.commit()
