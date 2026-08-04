# Inventory Management System

A simple command-line inventory management system built with Python, demonstrating OOP design, CRUD operations, JSON persistence, and input validation.

## Structure

- `InventoryItem` — represents a single product with `product_id`, `name`, `quantity`, and `price`. Supports `to_dict()` / `from_dict()` for JSON serialization.
- `Inventory` — manages a collection of products (keyed by `product_id`) and provides CRUD operations plus JSON save/load.

## Features

- **Add Product** — add a new product; rejects duplicate product IDs, negative quantity, or price ≤ 0.
- **Update Product** — update name, quantity, and/or price of an existing product.
- **Delete Product** — remove a product by ID.
- **Search Product** — search by product ID or by (partial, case-insensitive) name.
- **Display Products** — list all products in inventory.
- **Save** — persist current inventory to `inventory.json`.
- **Exit** — saves inventory to `inventory.json` before exiting.

## Validation Rules

- Product IDs must be unique.
- Quantity cannot be negative.
- Price must be greater than zero.

Invalid input raises a `ValueError` with a descriptive message.

## Usage

```bash
python inventory_management.py
```

Follow the on-screen menu:

```
1. Add Product
2. Update Product
3. Delete Product
4. Search Product
5. Display Products
6. Save
7. Exit
```

Inventory data is persisted to `inventory.json` in the same directory.
