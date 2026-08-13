"""
supplier.py

Defines the Supplier dataclass - a single supplier with an ID, name,
email, and phone, plus conversion to/from a plain tuple so it can be
(de)serialized to/from a SQLite row.
"""

from dataclasses import dataclass


@dataclass
class Supplier:
    """Represents a single supplier."""

    supplier_id: str
    name: str
    email: str
    phone: str

    def to_row(self):
        """Convert the Supplier instance into a tuple matching the suppliers table's column order."""
        return (self.supplier_id, self.name, self.email, self.phone)

    @classmethod
    def from_row(cls, row):
        """Build a Supplier instance from a SQLite row (supplier_id, name, email, phone)."""
        supplier_id, name, email, phone = row
        return cls(supplier_id=supplier_id, name=name, email=email, phone=phone)

    def __str__(self):
        return f"ID: {self.supplier_id} | {self.name} | {self.email} | {self.phone}"
