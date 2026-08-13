"""
product.py

Defines the Product dataclass - a single product with an ID, name,
category, price, quantity, and a supplier ID (foreign key), plus
conversion to/from a plain tuple so it can be (de)serialized to/from a
SQLite row.
"""

from dataclasses import dataclass


@dataclass
class Product:
    """Represents a single product."""

    product_id: str
    name: str
    category: str
    price: float
    quantity: int
    supplier_id: str

    def to_row(self):
        """Convert the Product instance into a tuple matching the products table's column order."""
        return (
            self.product_id,
            self.name,
            self.category,
            self.price,
            self.quantity,
            self.supplier_id,
        )

    @classmethod
    def from_row(cls, row):
        """Build a Product instance from a SQLite row (product_id, name, category, price, quantity, supplier_id)."""
        product_id, name, category, price, quantity, supplier_id = row
        return cls(
            product_id=product_id,
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            supplier_id=supplier_id,
        )

    def __str__(self):
        return (
            f"ID: {self.product_id} | {self.name} | Category: {self.category} | "
            f"Price: {self.price:.2f} | Qty: {self.quantity} | Supplier: {self.supplier_id}"
        )
