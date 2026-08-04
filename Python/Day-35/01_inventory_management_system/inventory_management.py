import json
import os


class InventoryItem:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["quantity"],
            data["price"],
        )

    def __str__(self):
        return (
            f"ID: {self.product_id} | Name: {self.name} | "
            f"Qty: {self.quantity} | Price: {self.price:.2f}"
        )


class Inventory:
    def __init__(self, json_file="inventory.json"):
        self.products = {}
        self.json_file = json_file

    def add_product(self, product_id, name, quantity, price):
        if product_id in self.products:
            raise ValueError(f"Product ID '{product_id}' already exists.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        self.products[product_id] = InventoryItem(product_id, name, quantity, price)

    def update_product(self, product_id, name=None, quantity=None, price=None):
        if product_id not in self.products:
            raise ValueError(f"Product ID '{product_id}' does not exist.")

        item = self.products[product_id]

        if name is not None:
            item.name = name
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            item.quantity = quantity
        if price is not None:
            if price <= 0:
                raise ValueError("Price must be greater than zero.")
            item.price = price

    def delete_product(self, product_id):
        if product_id not in self.products:
            raise ValueError(f"Product ID '{product_id}' does not exist.")
        del self.products[product_id]

    def search_product(self, product_id=None, name=None):
        if product_id is not None:
            item = self.products.get(product_id)
            return [item] if item else []

        if name is not None:
            name_lower = name.lower()
            return [
                item
                for item in self.products.values()
                if name_lower in item.name.lower()
            ]

        return []

    def display_products(self):
        if not self.products:
            print("No products in inventory.")
            return

        for item in self.products.values():
            print(item)

    def save_json(self):
        data = [item.to_dict() for item in self.products.values()]
        with open(self.json_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_json(self):
        if not os.path.exists(self.json_file):
            return

        with open(self.json_file, "r") as f:
            data = json.load(f)

        self.products = {
            entry["product_id"]: InventoryItem.from_dict(entry) for entry in data
        }


def prompt_int(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Please enter a valid integer.")


def prompt_float(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Please enter a valid number.")


def main():
    inventory = Inventory()
    inventory.load_json()

    menu = """
1. Add Product
2. Update Product
3. Delete Product
4. Search Product
5. Display Products
6. Save
7. Exit
"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            product_id = input("Product ID: ").strip()
            name = input("Name: ").strip()
            quantity = prompt_int("Quantity: ")
            price = prompt_float("Price: ")
            try:
                inventory.add_product(product_id, name, quantity, price)
                print("Product added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            product_id = input("Product ID to update: ").strip()
            name = input("New name (leave blank to keep unchanged): ").strip()
            quantity_input = input("New quantity (leave blank to keep unchanged): ").strip()
            price_input = input("New price (leave blank to keep unchanged): ").strip()

            try:
                quantity = int(quantity_input) if quantity_input else None
                price = float(price_input) if price_input else None
                inventory.update_product(
                    product_id,
                    name if name else None,
                    quantity,
                    price,
                )
                print("Product updated successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            product_id = input("Product ID to delete: ").strip()
            try:
                inventory.delete_product(product_id)
                print("Product deleted successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            sub_choice = input("Search by (1) Product ID or (2) Name: ").strip()
            if sub_choice == "1":
                product_id = input("Product ID: ").strip()
                results = inventory.search_product(product_id=product_id)
            else:
                name = input("Name: ").strip()
                results = inventory.search_product(name=name)

            if results:
                for item in results:
                    print(item)
            else:
                print("No matching products found.")

        elif choice == "5":
            inventory.display_products()

        elif choice == "6":
            inventory.save_json()
            print("Inventory saved.")

        elif choice == "7":
            inventory.save_json()
            print("Inventory saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
