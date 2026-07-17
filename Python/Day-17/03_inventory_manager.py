items = {}

def add_item():

    name = input("Enter item name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    items[name] = {"quantity": quantity, "price": price}

    print("Item added successfully.")

def view_items():

    for item, info in items.items():
        print(f"Name: {item}\nQuantity: {info['quantity']}\nPrice: {info['price']}\n")
        print("-----------------\n")

def search_item():

    name = input("Enter item name to search for: ")

    if name in items:
        info = items[name]
        print(f"\nItem Found:\nName: {name}\nQuantity: {info['quantity']}\nPrice: {info['price']}\n")

    else:
        print("Student not found.\n")

while True:
    choice = int(input("1. Add Item\n2. View Items\n3. Search Item\n4. Exit\n\nEnter choice: "))

    if choice == 1:
        add_item()
        continue

    elif choice == 2:
        view_items()
        continue

    elif choice == 3:
        search_item()
        continue

    elif choice == 4:
        print("Thank you for using Inventory Manager.")
        break

    else:
        print("Invalid Choice. Please pick 1, 2, 3, or 4.\n")
        continue
