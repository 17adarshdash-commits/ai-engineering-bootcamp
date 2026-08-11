"""
database.py

Owns the SQLite connection and schema for the student database system -
creating the database file/table if needed, and providing a single place
that opens/closes connections so no other module talks to sqlite3 directly.
"""

import sqlite3

DB_FILE = "students.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    cgpa REAL NOT NULL
)
"""


class Database:
    """Manages the SQLite connection for the students table."""

    def __init__(self, db_file=DB_FILE):
        self.db_file = db_file
        self._init_schema()

    def _init_schema(self):
        """Create the database file (if needed) and the students table (if needed)."""
        conn = self.connect()
        conn.execute(CREATE_TABLE_SQL)
        conn.commit()
        conn.close()

    def connect(self):
        """Open a fresh connection to the database file."""
        return sqlite3.connect(self.db_file)
