"""
main.py

Command-line interface for the Inventory Database System.
"""

from database import Database
from inventory_manager import InventoryError, InventoryManager

MENU = """
================ Inventory Database System ================
 Suppliers
  1. Add Supplier
  2. Update Supplier
  3. Delete Supplier
  4. Display Suppliers
 Products
  5. Add Product
  6. Update Product
  7. Delete Product
  8. Search Product
  9. Display Products
 Reports
  10. Products with Supplier Names
  11. Low Stock Report
  12. Inventory Value
  13. Products by Category
  14. Exit
==============================================================
"""


# ------------------------------------------------------------------
# Suppliers
# ------------------------------------------------------------------
def add_supplier(manager):
    supplier_id = input("Enter supplier ID: ").strip()
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()

    try:
        manager.add_supplier(supplier_id, name, email, phone)
        print("Supplier added successfully.")
    except InventoryError as e:
        print(f"Error: {e}")


def update_supplier(manager):
    supplier_id = input("Enter supplier ID to update: ").strip()
    print("Leave a field blank to keep its current value.")
    name = input("New name: ").strip()
    email = input("New email: ").strip()
    phone = input("New phone: ").strip()

    updates = {}
    if name:
        updates["name"] = name
    if email:
        updates["email"] = email
    if phone:
        updates["phone"] = phone

    try:
        supplier = manager.update_supplier(supplier_id, **updates)
        print(f"Supplier updated: {supplier}")
    except InventoryError as e:
        print(f"Error: {e}")


def delete_supplier(manager):
    supplier_id = input("Enter supplier ID to delete: ").strip()
    try:
        manager.delete_supplier(supplier_id)
        print("Supplier deleted successfully.")
    except InventoryError as e:
        print(f"Error: {e}")


def display_suppliers(manager):
    suppliers = manager.display_suppliers()
    if not suppliers:
        print("No suppliers to display.")
        return
    for supplier in suppliers:
        print(supplier)


# ------------------------------------------------------------------
# Products
# ------------------------------------------------------------------
def add_product(manager):
    product_id = input("Enter product ID: ").strip()
    name = input("Enter name: ").strip()
    category = input("Enter category: ").strip()
    price = input("Enter price: ").strip()
    quantity = input("Enter quantity: ").strip()
    supplier_id = input("Enter supplier ID: ").strip()

    try:
        manager.add_product(product_id, name, category, price, quantity, supplier_id)
        print("Product added successfully.")
    except InventoryError as e:
        print(f"Error: {e}")


def update_product(manager):
    product_id = input("Enter product ID to update: ").strip()
    print("Leave a field blank to keep its current value.")
    name = input("New name: ").strip()
    category = input("New category: ").strip()
    price = input("New price: ").strip()
    quantity = input("New quantity: ").strip()
    supplier_id = input("New supplier ID: ").strip()

    updates = {}
    if name:
        updates["name"] = name
    if category:
        updates["category"] = category
    if price:
        updates["price"] = price
    if quantity:
        updates["quantity"] = quantity
    if supplier_id:
        updates["supplier_id"] = supplier_id

    try:
        product = manager.update_product(product_id, **updates)
        print(f"Product updated: {product}")
    except InventoryError as e:
        print(f"Error: {e}")


def delete_product(manager):
    product_id = input("Enter product ID to delete: ").strip()
    try:
        manager.delete_product(product_id)
        print("Product deleted successfully.")
    except InventoryError as e:
        print(f"Error: {e}")


def search_product(manager):
    keyword = input("Enter search keyword (ID/name/category): ").strip()
    results = manager.search_product(keyword)
    if not results:
        print("No matching products found.")
        return
    for product in results:
        print(product)


def display_products(manager):
    products = manager.display_products()
    if not products:
        print("No products to display.")
        return
    for product in products:
        print(product)


# ------------------------------------------------------------------
# Reports
# ------------------------------------------------------------------
def products_with_supplier_names(manager):
    rows = manager.products_with_supplier_names()
    if not rows:
        print("No products to report.")
        return
    for name, category, price, quantity, supplier_name in rows:
        print(f"{name} ({category}) | Price: {price:.2f} | Qty: {quantity} | Supplier: {supplier_name}")


def low_stock_report(manager):
    threshold_input = input(
        f"Enter low stock threshold (blank for default {5}): "
    ).strip()
    threshold = int(threshold_input) if threshold_input else 5

    rows = manager.low_stock_report(threshold)
    if not rows:
        print("No products at or below that threshold.")
        return
    for product_id, name, category, quantity in rows:
        print(f"ID: {product_id} | {name} ({category}) | Qty: {quantity}")


def inventory_value(manager):
    total = manager.inventory_value()
    print(f"Total inventory value: {total:.2f}")


def products_by_category(manager):
    rows = manager.products_by_category()
    if not rows:
        print("No products to report.")
        return
    for category, count, total_quantity in rows:
        print(f"{category}: {count} product(s), {total_quantity} total units")


def main():
    database = Database()
    manager = InventoryManager(database)

    actions = {
        "1": add_supplier,
        "2": update_supplier,
        "3": delete_supplier,
        "4": display_suppliers,
        "5": add_product,
        "6": update_product,
        "7": delete_product,
        "8": search_product,
        "9": display_products,
        "10": products_with_supplier_names,
        "11": low_stock_report,
        "12": inventory_value,
        "13": products_by_category,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "14":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(manager)


if __name__ == "__main__":
    main()
