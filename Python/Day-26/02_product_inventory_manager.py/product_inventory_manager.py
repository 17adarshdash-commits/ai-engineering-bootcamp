import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(SCRIPT_DIR, "products.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "inventory_report.txt")
DATE_FORMAT = "%Y-%m-%d"


def load_products():
    products = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                product_id, name, category, quantity, price, date_added = [
                    part.strip() for part in line.split(",")
                ]

                products[product_id] = {
                    "name": name,
                    "category": category,
                    "quantity": int(quantity),
                    "price": float(price),
                    "date_added": date_added,
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
                f"{product_id}, {info['name']}, {info['category']}, "
                f"{info['quantity']}, {info['price']}, {info['date_added']}\n"
            )


products = load_products()


def format_header(title, width=5):
    return f"{'=' * width} {title} {'=' * width}"


def find_product(product_id):
    return products.get(product_id)


def notify_if_empty():
    if not products:
        print("Product Inventory is empty.\n")
        return True
    return False


def display_product(product_id, info):
    print(f"ID: {product_id}")
    print(f"Name: {info['name']}")
    print(f"Category: {info['category']}")
    print(f"Quantity: {info['quantity']}")
    print(f"Price: {info['price']}")
    print(f"Date Added: {info['date_added']}")
    print("-----------------")


def get_unique_product_id():
    while True:
        product_id = input("Enter Product ID: ").strip()
        if not product_id:
            print("Product ID cannot be empty.")
            continue
        if product_id in products:
            print("Product ID already exists.")
            continue
        return product_id


def get_valid_name():
    while True:
        name = input("Enter Product Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        return name


def get_valid_category():
    while True:
        category = input("Enter Category: ").strip()
        if not category:
            print("Category cannot be empty.")
            continue
        return category


def get_valid_quantity():
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Quantity must be an integer.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue
        return quantity


def get_valid_price():
    while True:
        try:
            price = float(input("Enter Price: "))
        except ValueError:
            print("Price must be a number.")
            continue
        if price <= 0:
            print("Price must be greater than 0.")
            continue
        return price


def add_product():
    product_id = get_unique_product_id()
    name = get_valid_name()
    category = get_valid_category()
    quantity = get_valid_quantity()
    price = get_valid_price()
    date_added = datetime.now().strftime(DATE_FORMAT)

    products[product_id] = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "date_added": date_added,
    }
    save_products()
    print("Product added successfully.")


def view_products():
    if notify_if_empty():
        return
    for product_id, info in products.items():
        display_product(product_id, info)


def search_product():
    if notify_if_empty():
        return
    query = input("Enter Product ID or Name: ").strip().lower()
    found = False
    for product_id, info in products.items():
        if query in product_id.lower() or query in info["name"].lower():
            display_product(product_id, info)
            found = True
    if not found:
        print("Product not found.")


def update_quantity():
    if notify_if_empty():
        return
    product_id = input("Enter Product ID: ").strip()
    info = find_product(product_id)
    if info is None:
        print("Product not found.")
        return

    quantity = get_valid_quantity()
    info["quantity"] = quantity
    save_products()
    print("Quantity updated successfully.")


def delete_product():
    if notify_if_empty():
        return
    product_id = input("Enter Product ID: ").strip()
    if find_product(product_id) is not None:
        del products[product_id]
        save_products()
        print("Product deleted successfully.")
    else:
        print("Product not found.")


def get_total_inventory_value():
    return sum(info["quantity"] * info["price"] for info in products.values())


def get_highest_value_product():
    product_id = max(products, key=lambda p: products[p]["quantity"] * products[p]["price"])
    return product_id, products[product_id]


def get_category_counts():
    categories = {}
    for info in products.values():
        categories[info["category"]] = categories.get(info["category"], 0) + 1
    return categories


def generate_report():
    if notify_if_empty():
        return

    total_value = get_total_inventory_value()
    highest_id, highest_info = get_highest_value_product()
    categories = get_category_counts()

    with open(REPORT_FILE, "w") as file:
        file.write(f"{format_header('INVENTORY REPORT', 10)}\n\n")
        file.write("Generated On:\n")
        file.write(f"{datetime.now().strftime(DATE_FORMAT)}\n\n")
        file.write("Total Products:\n")
        file.write(f"{len(products)}\n\n")
        file.write("Total Inventory Value:\n")
        file.write(f"£{total_value:.0f}\n\n")
        file.write("Highest Value Product:\n")
        file.write(f"{highest_info['name']}\n\n")
        file.write("Products Per Category\n\n")
        for category, count in sorted(categories.items()):
            file.write(f"{category} : {count}\n")
        file.write("\n--------------------------------\n\n")

        file.write("Complete Product List\n\n")
        file.write(f"{'ID':<8}{'Name':<15}{'Category':<15}{'Quantity':<10}{'Price':<10}{'Date Added'}\n\n")
        for product_id, info in sorted(products.items()):
            file.write(
                f"{product_id:<8}{info['name']:<15}{info['category']:<15}"
                f"{info['quantity']:<10}{info['price']:<10}{info['date_added']}\n"
            )

    print("Inventory report generated to inventory_report.txt.")


while True:
    choice = input(
        f"{format_header('Product Inventory')}\n"
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
        print("Thank you for using the Product Inventory Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-7.")

    print()
