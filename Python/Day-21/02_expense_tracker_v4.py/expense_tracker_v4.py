import os
from datetime import date

CATEGORIES = ["Food", "Travel", "Shopping", "Entertainment", "Bills", "Other"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSES_FILE = os.path.join(BASE_DIR, "expenses.txt")
REPORT_FILE = os.path.join(BASE_DIR, "expense_report.txt")

def load_expenses():
    expenses = {}
    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, amount, category, expense_date = line.split(",")
                expenses[name] = {
                    "amount": float(amount),
                    "category": category,
                    "date": expense_date,
                }
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        for name, details in expenses.items():
            file.write(f"{name},{details['amount']},{details['category']},{details['date']}\n")

expenses = load_expenses()

def choose_category():
    print("Choose a category:")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    while True:
        choice = input("Enter category number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print(f"Invalid category. Please enter a number between 1 and {len(CATEGORIES)}.")

def add_expense():
    name = input("Enter Expense Name: ")
    try:
        amount = float(input("Enter Expense Amount: "))
        category = choose_category()
        expenses[name] = {
            "amount": amount,
            "category": category,
            "date": str(date.today()),
        }
        save_expenses(expenses)
        print("Expense added.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for name, details in expenses.items():
            print(f"{name}: ₹{details['amount']} | {details['category']} | {details['date']}")

def delete_expense():
    name = input("Enter Expense Name to delete: ")
    if name in expenses:
        del expenses[name]
        save_expenses(expenses)
        print("Expense Deleted.")
    else:
        print("Expense not found.")

def total_expenditure():
    total = sum(details["amount"] for details in expenses.values())
    print(f"Total Expenditure: {total}")

def edit_expense():
    name = input("Enter Expense Name to edit: ")
    if name in expenses:
        try:
            amount = float(input("Enter New Expense Amount: "))
            category = choose_category()
            expenses[name]["amount"] = amount
            expenses[name]["category"] = category
            save_expenses(expenses)
            print("Expense updated.")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    else:
        print("Expense not found. Cannot edit.")

def search_expense():
    name = input("Enter Expense Name to search for: ")
    if name in expenses:
        details = expenses[name]
        print(f"{name}: ₹{details['amount']} | {details['category']} | {details['date']}")
    else:
        print("Expense Not Found.")

def highest_expense():
    if not expenses:
        print("No expenses to evaluate.")
    else:
        highest_name = max(expenses, key=lambda n: expenses[n]["amount"])
        print(f"Highest Expense: {highest_name} ({expenses[highest_name]['amount']})")

def lowest_expense():
    if not expenses:
        print("No expenses to evaluate.")
    else:
        lowest_name = min(expenses, key=lambda n: expenses[n]["amount"])
        print(f"Lowest Expense: {lowest_name} ({expenses[lowest_name]['amount']})")

def sort_expense():
    if not expenses:
        print("No expenses to sort.")
        return

    print("Sort by:\n1. Amount (ascending)\n2. Amount (descending)\n3. Name (alphabetically)")
    choice = input("Enter choice: ")

    if choice == "1":
        sorted_expenses = sorted(expenses.items(), key=lambda item: item[1]["amount"])
    elif choice == "2":
        sorted_expenses = sorted(expenses.items(), key=lambda item: item[1]["amount"], reverse=True)
    elif choice == "3":
        sorted_expenses = sorted(expenses.items(), key=lambda item: item[0].lower())
    else:
        print("Invalid choice.")
        return

    for name, details in sorted_expenses:
        print(f"{name}: ₹{details['amount']} | {details['category']} | {details['date']}")

def expense_report():
    if not expenses:
        print("No expenses to report.")
        return

    amounts = [details["amount"] for details in expenses.values()]
    total = sum(amounts)
    count = len(amounts)
    average = total / count

    by_category = {category: 0 for category in CATEGORIES}
    for details in expenses.values():
        by_category[details["category"]] += details["amount"]

    lines = []
    lines.append("========== EXPENSE REPORT ==========")
    lines.append("")
    lines.append("Generated On:")
    lines.append(str(date.today()))
    lines.append("")
    lines.append("Total Expenses:")
    lines.append(f"₹{total:,.2f}")
    lines.append("")
    lines.append("Total Transactions:")
    lines.append(str(count))
    lines.append("")
    lines.append("Highest Expense:")
    lines.append(f"₹{max(amounts):,.2f}")
    lines.append("")
    lines.append("Lowest Expense:")
    lines.append(f"₹{min(amounts):,.2f}")
    lines.append("")
    lines.append("Average Expense:")
    lines.append(f"₹{average:,.2f}")
    lines.append("")
    lines.append("Expenses by Category")
    lines.append("")
    for category in CATEGORIES:
        if by_category[category] > 0:
            lines.append(f"{category}:")
            lines.append(f"₹{by_category[category]:,.2f}")
            lines.append("")

    report_text = "\n".join(lines)

    with open(REPORT_FILE, "w") as file:
        file.write(report_text)

    print(report_text)
    print("\nReport saved to expense_report.txt")

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense\n2. View Expenses\n3. Total Expenditure")
    print("4. Delete Expense\n5. Edit Expense\n6. Search Expense")
    print("7. Highest Expense\n8. Lowest Expense\n9. Sort Expenses")
    print("10. Expense Report\n11. Exit")

    try:
        choice = int(input("\nEnter choice: "))
    except ValueError:
        print("Invalid Choice. Please enter a number between 1 and 11.")
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
        expense_report()
    elif choice == 11:
        print("Thank you for using Expense Tracker.")
        break
    else:
        print("Invalid Choice. Please pick a number from 1 to 11.")
