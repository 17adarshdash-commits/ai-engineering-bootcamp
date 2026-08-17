"""database.py - SQLite connection handling and schema setup.

Owns the one thing every other module needs: a short-lived connection to
tasks.db, with dict-like row access, and the DDL for the tasks table.
Nothing here knows about FastAPI or Pydantic - just SQLite.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "tasks.db"


def get_connection() -> sqlite3.Connection:
    """Open a fresh connection. Callers are responsible for closing it."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Create the tasks table if it doesn't already exist.

    id is client-supplied (not autoincrement) so that duplicate-id
    validation on create has something to check against.
    """
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()
