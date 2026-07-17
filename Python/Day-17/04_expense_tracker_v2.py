expenses = {}

def add_expense():
    name = input("Enter Expense Name: ")
    try:
        amount = float(input("Enter Expense Amount: "))
        expenses[name] = amount
        print("Expense added.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for name, amount in expenses.items():
            print(f"{name}: {amount}")

def delete_expense():
    name = input("Enter Expense Name to delete: ")
    if name in expenses:
        del expenses[name]
        print("Expense Deleted.")
    else:
        print("Expense not found.")

def total_expenditure():
    total = sum(expenses.values())
    print(f"Total Expenditure: {total}")

def edit_expense():
    name = input("Enter Expense Name to edit: ")
    if name in expenses:
        try:
            amount = float(input("Enter New Expense Amount: "))
            expenses[name] = amount
            print("Expense updated.")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    else:
        print("Expense not found. Cannot edit.")

def search_expense():
    name = input("Enter Expense Name to search for: ")
    if name in expenses:
        print(f"{name}: {expenses[name]}")
    else:
        print("Expense Not Found.")

def highest_expense():
    if not expenses:
        print("No expenses to evaluate.")
    else:
        # This finds the name of the highest expense, not just the number
        highest_name = max(expenses, key=expenses.get)
        print(f"Highest Expense: {highest_name} ({expenses[highest_name]})")

def lowest_expense():
    if not expenses:
        print("No expenses to evaluate.")
    else:
        lowest_name = min(expenses, key=expenses.get)
        print(f"Lowest Expense: {lowest_name} ({expenses[lowest_name]})")

def sort_expense():
    if not expenses:
        print("No expenses to sort.")
        return

    print("Sort by:\n1. Amount (ascending)\n2. Amount (descending)\n3. Name (alphabetically)")
    choice = input("Enter choice: ")

    if choice == "1":
        sorted_expenses = sorted(expenses.items(), key=lambda item: item[1])
    elif choice == "2":
        sorted_expenses = sorted(expenses.items(), key=lambda item: item[1], reverse=True)
    elif choice == "3":
        sorted_expenses = sorted(expenses.items(), key=lambda item: item[0].lower())
    else:
        print("Invalid choice.")
        return

    for name, amount in sorted_expenses:
        print(f"{name}: {amount}")

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense\n2. View Expenses\n3. Total Expenditure")
    print("4. Delete Expense\n5. Edit Expense\n6. Search Expense")
    print("7. Highest Expense\n8. Lowest Expense\n9. Sort Expenses\n10. Exit")

    try:
        choice = int(input("\nEnter choice: "))
    except ValueError:
        print("Invalid Choice. Please enter a number between 1 and 10.")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_expenditure()
    elif choice == 4:
        delete_expense()
    elif choice == 5:
        edit_expense()
    elif choice == 6:
        search_expense()
    elif choice == 7:
        highest_expense()
    elif choice == 8:
        lowest_expense()
    elif choice == 9:
        sort_expense()
    elif choice == 10:
        print("Thank you for using Expense Tracker.")
        break
    else:
        print("Invalid Choice. Please pick a number from 1 to 10.")