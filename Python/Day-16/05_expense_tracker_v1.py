expenses = {}

def add_expense():

    name = input("Enter Expense Name: ")
    amount = float(input("Enter Expense Amount: "))

    expenses[name] = amount

    print("Expense added.")

def view_expenses():

    for name,amount in expenses.items():
        print(f"{name}: {amount}")

def delete_expense():

    name = input("Enter Expense Name to delete: ")
    del expenses[name]
    print("Expense Deleted.")

def total_expenditure():

    total = 0

    for amount in expenses.values():
        total += amount

    print(f"Total Expenditure: {total}")

while True:

    choice = int(input("1. Add Expense\n2. View Expenses\n3. Total Expenditure\n4. Delete Expense\n5. Exit\n\nEnter choice: "))

    if choice == 1:
        add_expense()
        continue

    elif choice == 2:
        view_expenses()
        continue

    elif choice == 3:
        total_expenditure()
        continue

    elif choice == 4:
        delete_expense()
        continue

    elif choice == 5:
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("Invalid Choice. Please pick 1, 2, 3, or 4.\n")
        continue