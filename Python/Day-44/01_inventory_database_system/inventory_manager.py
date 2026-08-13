"""
inventory_manager.py

Defines InventoryManager - validates input and performs every supplier/
product/report operation against the suppliers and products tables,
using a Database instance for every connection. All SQL here uses '?'
placeholders. Multi-step writes are wrapped in explicit transactions
(commit on success, rollback on failure).
"""

import sqlite3

from product import Product
from supplier import Supplier

MIN_QUANTITY = 0
LOW_STOCK_THRESHOLD = 5


class InventoryError(Exception):
    """Base exception for all inventory-related errors."""


# -- Supplier errors ------------------------------------------------------
class DuplicateSupplierIDError(InventoryError):
    """Raised when a supplier ID already exists."""


class InvalidSupplierNameError(InventoryError):
    """Raised when a supplier name is empty/blank."""


class InvalidEmailError(InventoryError):
    """Raised when an email fails basic validation."""


class DuplicateEmailError(InventoryError):
    """Raised when an email is already used by another supplier."""


class InvalidPhoneError(InventoryError):
    """Raised when a supplier phone is empty/blank."""


class SupplierNotFoundError(InventoryError):
    """Raised when a supplier ID cannot be found."""


class SupplierHasProductsError(InventoryError):
    """Raised when deleting a supplier that still has products referencing it."""


# -- Product errors ------------------------------------------------------
class DuplicateProductIDError(InventoryError):
    """Raised when a product ID already exists."""


class InvalidProductNameError(InventoryError):
    """Raised when a product name is empty/blank."""


class InvalidCategoryError(InventoryError):
    """Raised when a product category is empty/blank."""


class InvalidPriceError(InventoryError):
    """Raised when a price is not a positive number."""


class InvalidQuantityError(InventoryError):
    """Raised when a quantity is not a non-negative integer."""


class ProductNotFoundError(InventoryError):
    """Raised when a product ID cannot be found."""


class InventoryManager:
    """Performs validated operations on suppliers and products."""

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
    def _validate_email(email):
        if not email or "@" not in email or "." not in email.split("@")[-1]:
            raise InvalidEmailError(f"'{email}' is not a valid email address.")

    @staticmethod
    def _validate_price(price):
        try:
            price = float(price)
        except (TypeError, ValueError):
            raise InvalidPriceError("Price must be a number.")
        if price <= 0:
            raise InvalidPriceError("Price must be greater than 0.")
        return price

    @staticmethod
    def _validate_quantity(quantity):
        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            raise InvalidQuantityError("Quantity must be an integer.")
        if quantity < MIN_QUANTITY:
            raise InvalidQuantityError("Quantity cannot be negative.")
        return quantity

    # ------------------------------------------------------------------
    # Suppliers - Create
    # ------------------------------------------------------------------
    def add_supplier(self, supplier_id, name, email, phone):
        """Add a new supplier after validating all fields."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT 1 FROM suppliers WHERE supplier_id = ?", (supplier_id,)
            )
            if cursor.fetchone() is not None:
                raise DuplicateSupplierIDError(f"Supplier ID '{supplier_id}' already exists.")

            self._validate_non_empty(name, InvalidSupplierNameError, "Name")
            self._validate_email(email)
            self._validate_non_empty(phone, InvalidPhoneError, "Phone")

            cursor = conn.execute("SELECT 1 FROM suppliers WHERE email = ?", (email,))
            if cursor.fetchone() is not None:
                raise DuplicateEmailError(f"Email '{email}' is already registered.")

            supplier = Supplier(
                supplier_id=supplier_id, name=name.strip(), email=email.strip(), phone=phone.strip()
            )
            conn.execute(
                "INSERT INTO suppliers (supplier_id, name, email, phone) VALUES (?, ?, ?, ?)",
                supplier.to_row(),
            )
            conn.commit()
            return supplier
        except InventoryError:
            conn.rollback()
            raise
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Suppliers - Read
    # ------------------------------------------------------------------
    def get_supplier(self, supplier_id):
        """Fetch a single supplier by id, or raise SupplierNotFoundError."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT supplier_id, name, email, phone FROM suppliers WHERE supplier_id = ?",
                (supplier_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise SupplierNotFoundError(f"Supplier ID '{supplier_id}' not found.")
            return Supplier.from_row(row)
        finally:
            conn.close()

    def display_suppliers(self):
        """Return every supplier, ordered by name."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT supplier_id, name, email, phone FROM suppliers ORDER BY name"
            )
            return [Supplier.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Suppliers - Update
    # ------------------------------------------------------------------
    def update_supplier(self, supplier_id, **updates):
        """Update one or more fields of an existing supplier."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT 1 FROM suppliers WHERE supplier_id = ?", (supplier_id,)
            )
            if cursor.fetchone() is None:
                raise SupplierNotFoundError(f"Supplier ID '{supplier_id}' not found.")

            fields = {}
            if "name" in updates:
                self._validate_non_empty(updates["name"], InvalidSupplierNameError, "Name")
                fields["name"] = updates["name"].strip()
            if "email" in updates:
                self._validate_email(updates["email"])
                cursor = conn.execute(
                    "SELECT 1 FROM suppliers WHERE email = ? AND supplier_id != ?",
                    (updates["email"], supplier_id),
                )
                if cursor.fetchone() is not None:
                    raise DuplicateEmailError(f"Email '{updates['email']}' is already registered.")
                fields["email"] = updates["email"].strip()
            if "phone" in updates:
                self._validate_non_empty(updates["phone"], InvalidPhoneError, "Phone")
                fields["phone"] = updates["phone"].strip()

            if not fields:
                return self.get_supplier(supplier_id)

            set_clause = ", ".join(f"{column} = ?" for column in fields)
            values = list(fields.values()) + [supplier_id]
            conn.execute(f"UPDATE suppliers SET {set_clause} WHERE supplier_id = ?", values)
            conn.commit()
            return self.get_supplier(supplier_id)
        except InventoryError:
            conn.rollback()
            raise
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Suppliers - Delete
    # ------------------------------------------------------------------
    def delete_supplier(self, supplier_id):
        """Delete a supplier by id, refusing if products still reference it."""
        conn = self.database.connect()
        try:
            try:
                cursor = conn.execute(
                    "DELETE FROM suppliers WHERE supplier_id = ?", (supplier_id,)
                )
                conn.commit()
            except sqlite3.IntegrityError:
                conn.rollback()
                raise SupplierHasProductsError(
                    f"Supplier ID '{supplier_id}' has products and cannot be deleted."
                )
            if cursor.rowcount == 0:
                raise SupplierNotFoundError(f"Supplier ID '{supplier_id}' not found.")
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Products - Create
    # ------------------------------------------------------------------
    def add_product(self, product_id, name, category, price, quantity, supplier_id):
        """Add a new product after validating all fields and the supplier reference."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT 1 FROM products WHERE product_id = ?", (product_id,)
            )
            if cursor.fetchone() is not None:
                raise DuplicateProductIDError(f"Product ID '{product_id}' already exists.")

            self._validate_non_empty(name, InvalidProductNameError, "Name")
            self._validate_non_empty(category, InvalidCategoryError, "Category")
            price = self._validate_price(price)
            quantity = self._validate_quantity(quantity)

            cursor = conn.execute(
                "SELECT 1 FROM suppliers WHERE supplier_id = ?", (supplier_id,)
            )
            if cursor.fetchone() is None:
                raise SupplierNotFoundError(f"Supplier ID '{supplier_id}' not found.")

            product = Product(
                product_id=product_id,
                name=name.strip(),
                category=category.strip(),
                price=price,
                quantity=quantity,
                supplier_id=supplier_id,
            )
            conn.execute(
                "INSERT INTO products (product_id, name, category, price, quantity, supplier_id) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                product.to_row(),
            )
            conn.commit()
            return product
        except InventoryError:
            conn.rollback()
            raise
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Products - Read
    # ------------------------------------------------------------------
    def get_product(self, product_id):
        """Fetch a single product by id, or raise ProductNotFoundError."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT product_id, name, category, price, quantity, supplier_id "
                "FROM products WHERE product_id = ?",
                (product_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise ProductNotFoundError(f"Product ID '{product_id}' not found.")
            return Product.from_row(row)
        finally:
            conn.close()

    def display_products(self):
        """Return every product, ordered by name."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT product_id, name, category, price, quantity, supplier_id "
                "FROM products ORDER BY name"
            )
            return [Product.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    def search_product(self, keyword):
        """Search products by ID, name, or category (case-insensitive substring match)."""
        conn = self.database.connect()
        try:
            pattern = f"%{keyword}%"
            cursor = conn.execute(
                """
                SELECT product_id, name, category, price, quantity, supplier_id FROM products
                WHERE product_id LIKE ? OR name LIKE ? OR category LIKE ?
                ORDER BY name
                """,
                (pattern, pattern, pattern),
            )
            return [Product.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Products - Update
    # ------------------------------------------------------------------
    def update_product(self, product_id, **updates):
        """Update one or more fields of an existing product."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT 1 FROM products WHERE product_id = ?", (product_id,)
            )
            if cursor.fetchone() is None:
                raise ProductNotFoundError(f"Product ID '{product_id}' not found.")

            fields = {}
            if "name" in updates:
                self._validate_non_empty(updates["name"], InvalidProductNameError, "Name")
                fields["name"] = updates["name"].strip()
            if "category" in updates:
                self._validate_non_empty(updates["category"], InvalidCategoryError, "Category")
                fields["category"] = updates["category"].strip()
            if "price" in updates:
                fields["price"] = self._validate_price(updates["price"])
            if "quantity" in updates:
                fields["quantity"] = self._validate_quantity(updates["quantity"])
            if "supplier_id" in updates:
                cursor = conn.execute(
                    "SELECT 1 FROM suppliers WHERE supplier_id = ?", (updates["supplier_id"],)
                )
                if cursor.fetchone() is None:
                    raise SupplierNotFoundError(f"Supplier ID '{updates['supplier_id']}' not found.")
                fields["supplier_id"] = updates["supplier_id"]

            if not fields:
                return self.get_product(product_id)

            set_clause = ", ".join(f"{column} = ?" for column in fields)
            values = list(fields.values()) + [product_id]
            conn.execute(f"UPDATE products SET {set_clause} WHERE product_id = ?", values)
            conn.commit()
            return self.get_product(product_id)
        except InventoryError:
            conn.rollback()
            raise
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Products - Delete
    # ------------------------------------------------------------------
    def delete_product(self, product_id):
        """Delete a product by id."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise ProductNotFoundError(f"Product ID '{product_id}' not found.")
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Reports
    # ------------------------------------------------------------------
    def products_with_supplier_names(self):
        """Every product alongside its supplier's name (INNER JOIN)."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                """
                SELECT products.name, products.category, products.price,
                       products.quantity, suppliers.name
                FROM products
                INNER JOIN suppliers ON products.supplier_id = suppliers.supplier_id
                ORDER BY products.name
                """
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def low_stock_report(self, threshold=LOW_STOCK_THRESHOLD):
        """Every product at or below the given quantity threshold."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                """
                SELECT product_id, name, category, quantity
                FROM products
                WHERE quantity <= ?
                ORDER BY quantity
                """,
                (threshold,),
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def inventory_value(self):
        """Total inventory value: SUM(price * quantity) across every product."""
        conn = self.database.connect()
        try:
            cursor = conn.execute("SELECT SUM(price * quantity) FROM products")
            total = cursor.fetchone()[0]
            return total if total is not None else 0.0
        finally:
            conn.close()

    def products_by_category(self):
        """Per-category product count and total quantity, via GROUP BY."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                """
                SELECT category, COUNT(*), SUM(quantity)
                FROM products
                GROUP BY category
                ORDER BY category
                """
            )
            return cursor.fetchall()
        finally:
            conn.close()
