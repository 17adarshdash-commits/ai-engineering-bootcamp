# Inventory Database System

A command-line inventory database system built as a multi-module Python
package, demonstrating SQLite persistence across two related tables
(with real foreign keys), transactions, indexes, JOINs, and validation -
the same modular architecture used in recent projects (`database.py` /
model / manager / `main.py`).

## Project Structure

```
01_inventory_database_system/
├── database.py           # Database - connection + automatic table/index creation (foreign keys ON)
├── product.py             # Product dataclass (to_row/from_row for SQLite rows)
├── supplier.py             # Supplier dataclass (to_row/from_row for SQLite rows)
├── inventory_manager.py     # InventoryManager - validated supplier/product/report operations
├── main.py                   # CLI entry point
├── inventory.db                # SQLite data file (created automatically on first run)
└── README.md
```

## Database Design

**Products** - `product_id` (PK), `name`, `category`, `price`
(`CHECK (price > 0)`), `quantity` (`CHECK (quantity >= 0)`),
`supplier_id` (FK -> Suppliers).

**Suppliers** - `supplier_id` (PK), `name`, `email` (`UNIQUE`), `phone`.

Products and Suppliers are one-to-many: one supplier can supply many
products, but each product has exactly one supplier.

## Features

- Create the database and both tables automatically on startup
- **Suppliers** - Add, Update, Delete, Display
- **Products** - Add, Update, Delete, Search (by ID/name/category),
  Display
- **Reports**
  - Products with Supplier Names (`INNER JOIN` products with suppliers)
  - Low Stock Report (products at or below a quantity threshold)
  - Inventory Value (`SUM(price * quantity)` across every product)
  - Products by Category (`GROUP BY category` - count and total quantity
    per category)

## Validation

- Product/Supplier IDs must be unique (`DuplicateProductIDError`,
  `DuplicateSupplierIDError`)
- Names and categories cannot be empty (`InvalidProductNameError`,
  `InvalidCategoryError`, `InvalidSupplierNameError`)
- Price must be greater than 0 (`InvalidPriceError`, also enforced at
  the schema level with `CHECK (price > 0)`)
- Quantity must be a non-negative integer (`InvalidQuantityError`, also
  enforced at the schema level with `CHECK (quantity >= 0)`)
- A product's supplier ID must reference an existing supplier
  (`SupplierNotFoundError`)
- Email must contain `@` and a `.` in the domain part
  (`InvalidEmailError`) and must be unique across suppliers
  (`DuplicateEmailError`)
- Deleting a supplier that still has products referencing it is refused
  (`SupplierHasProductsError`) - the database's own foreign key
  constraint is what catches this

All custom exceptions derive from a common `InventoryError` base
(defined in `inventory_manager.py`), so the CLI can catch a single
exception type for user-facing error messages.

## SQL Concepts Used

- **Foreign Keys** - `products.supplier_id` references `suppliers`;
  enforced via `PRAGMA foreign_keys = ON` on every connection
- **Transactions** - every write in `inventory_manager.py` that can fail
  partway through validation rolls back on error instead of leaving a
  partial write; `commit()` only happens once every step has succeeded
- **INNER JOIN** - `products_with_supplier_names()` joins products to
  suppliers to show each product alongside its supplier's name
- **ORDER BY** - suppliers/products/report rows are always returned in a
  stable, readable order
- **Aggregate Functions** - `SUM(price * quantity)` for inventory value,
  `COUNT(*)` / `SUM(quantity)` with `GROUP BY category` for the
  products-by-category report
- **Indexes** - `idx_products_supplier_id` and `idx_products_category`
  speed up the JOIN and GROUP BY report queries above, at the (accepted,
  here small) cost of slightly slower writes to `products`

## SQL Safety

Every query in `inventory_manager.py` uses `?` placeholders for values -
never f-strings or string concatenation - so no user input can alter a
query's structure (SQL injection).

## Usage

```bash
cd 01_inventory_database_system
python main.py
```

Follow the on-screen menu to manage suppliers, manage products, and run
reports. `inventory.db` is created automatically the first time the
program runs.
