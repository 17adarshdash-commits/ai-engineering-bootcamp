"""
database.py

Owns the SQLite connection and schema for the inventory database system -
creating the database file/tables (with foreign keys enabled) if needed,
and providing a single place that opens/closes connections so no other
module talks to sqlite3 directly.
"""

import sqlite3

DB_FILE = "inventory.db"

CREATE_SUPPLIERS_SQL = """
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL
)
"""

CREATE_PRODUCTS_SQL = """
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL CHECK (price > 0),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    supplier_id TEXT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
)
"""

CREATE_PRODUCT_SUPPLIER_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_products_supplier_id
ON products(supplier_id)
"""

CREATE_PRODUCT_CATEGORY_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_products_category
ON products(category)
"""


class Database:
    """Manages the SQLite connection for the inventory system's tables."""

    def __init__(self, db_file=DB_FILE):
        self.db_file = db_file
        self._init_schema()

    def _init_schema(self):
        """Create the database file (if needed), every table, and indexes (if needed)."""
        conn = self.connect()
        conn.execute(CREATE_SUPPLIERS_SQL)
        conn.execute(CREATE_PRODUCTS_SQL)
        # Indexed because both columns are searched/joined on frequently:
        # supplier_id in every "products with supplier names" report join,
        # category in the "products by category" report.
        conn.execute(CREATE_PRODUCT_SUPPLIER_INDEX_SQL)
        conn.execute(CREATE_PRODUCT_CATEGORY_INDEX_SQL)
        conn.commit()
        conn.close()

    def connect(self):
        """Open a fresh connection to the database file with foreign keys enforced."""
        conn = sqlite3.connect(self.db_file)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
