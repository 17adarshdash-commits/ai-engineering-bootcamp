import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(SCRIPT_DIR, "inventory.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "inventory_report.txt")
DATE_FORMAT = "%Y-%m-%d"

CATEGORIES = ["Electronics", "Books", "Clothing", "Food", "Other"]


def load_products():
    products = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                product_id, name, category, quantity, date_added = [
                    part.strip() for part in line.split(",")
                ]

                products[product_id] = {
                    "name": name,
                    "category": category,
                    "quantity": int(quantity),
                    "date_added": date_added
                }
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Data file is corrupted or contains invalid formats.")
    return products


def save_products():
    with open(DATA_FILE, "w") as file:
        for product_id, info in products.items():
            file.write(
                f"{product_id}, {info['name']}, {info['category']}, {info['quantity']}, {info['date_added']}\n"
            )


products = load_products()


def display_product(product_id, info):
    print(f"Product ID: {product_id}\nName: {info['name']}\nCategory: {info['category']}\n"
          f"Quantity: {info['quantity']}\nDate Added: {info['date_added']}")
    print("-----------------")


def get_valid_product_id():
    while True:
        product_id = input("Enter Product ID: ").strip()
        if not product_id:
            print("Product ID cannot be empty.")
            continue
        if product_id in products:
            print("Product ID must be unique.")
            continue
        return product_id


def get_valid_name():
    while True:
        name = input("Enter Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        return name


def get_valid_category():
    options = ", ".join(CATEGORIES)
    while True:
        category = input(f"Enter Category ({options}): ").strip()
        matched = next((c for c in CATEGORIES if c.lower() == category.lower()), None)
        if not matched:
            print(f"Category must be one of: {options}.")
            continue
        return matched


def get_valid_quantity():
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Quantity must be an integer.")
            continue
        if quantity < 0:
            print("Quantity must be >= 0.")
            continue
        return quantity


def add_product():
    product_id = get_valid_product_id()
    name = get_valid_name()
    category = get_valid_category()
    quantity = get_valid_quantity()
    date_added = datetime.now().strftime(DATE_FORMAT)

    products[product_id] = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "date_added": date_added
    }
    save_products()
    print("Product added successfully.")


def view_products():
    if not products:
        print("Inventory Manager is empty.\n")
        return
    for product_id, info in products.items():
        display_product(product_id, info)


def search_product():
    term = input("Search by Product ID or Name: ").strip().lower()

    if term in (pid.lower() for pid in products):
        product_id = next(pid for pid in products if pid.lower() == term)
        display_product(product_id, products[product_id])
        return

    matches = [
        (pid, info) for pid, info in products.items()
        if term in info["name"].lower()
    ]
    if matches:
        for product_id, info in matches:
            display_product(product_id, info)
    else:
        print("Product not found.")


def update_quantity():
    product_id = input("Enter Product ID: ").strip()
    if product_id not in products:
        print("Product not found.")
        return

    quantity = get_valid_quantity()
    products[product_id]["quantity"] = quantity
    save_products()
    print("Quantity updated successfully.")


def delete_product():
    product_id = input("Enter Product ID: ").strip()
    if product_id in products:
        del products[product_id]
        save_products()
        print("Product deleted successfully.")
    else:
        print("Product not found.")


def generate_report():
    if not products:
        print("Inventory Manager is empty.\n")
        return

    total_products = len(products)
    total_quantity = sum(info["quantity"] for info in products.values())

    categories = {}
    for info in products.values():
        categories[info["category"]] = categories.get(info["category"], 0) + 1

    with open(REPORT_FILE, "w") as file:
        file.write("========== INVENTORY REPORT ==========\n\n")
        file.write("Generated On:\n")
        file.write(f"{datetime.now().strftime(DATE_FORMAT)}\n\n")
        file.write("Total Products:\n")
        file.write(f"{total_products}\n\n")
        file.write("Total Quantity:\n")
        file.write(f"{total_quantity}\n\n")
        file.write("Products Per Category\n\n")
        for category, count in sorted(categories.items()):
            file.write(f"{category} : {count}\n")
        file.write("\n--------------------------------\n\n")

        file.write("Complete Inventory\n\n")
        file.write(f"{'ID':<8}{'Name':<15}{'Category':<15}{'Quantity':<10}{'Date Added'}\n\n")
        for product_id, info in sorted(products.items()):
            file.write(
                f"{product_id:<8}{info['name']:<15}{info['category']:<15}{info['quantity']:<10}{info['date_added']}\n"
            )

    print("Inventory report generated to inventory_report.txt.")


while True:
    choice = input(
        "===== Inventory Manager =====\n"
        "1. Add Product\n"
        "2. View Products\n"
        "3. Search Product\n"
        "4. Update Quantity\n"
        "5. Delete Product\n"
        "6. Generate Report\n"
        "7. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_quantity()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        generate_report()
    elif choice == "7":
        print("Thank you for using the Inventory Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-7.")

    print()
