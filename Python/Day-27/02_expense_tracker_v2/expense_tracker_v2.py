import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "expenses.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "expense_report.txt")

DATE_FORMAT = "%Y-%m-%d"


def load_expenses():
    expenses = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                expense_id, category, amount, expense_date, description = line.split(",", 4)
                expenses[expense_id] = {
                    "category": category,
                    "amount": float(amount),
                    "date": expense_date,
                    "description": description,
                }
    except FileNotFoundError:
        pass
    return expenses


def save_expenses():
    with open(DATA_FILE, "w") as file:
        for expense_id, info in expenses.items():
            file.write(f"{expense_id},{info['category']},{info['amount']},{info['date']},{info['description']}\n")


expenses = load_expenses()


def format_header(title, width=5):
    return f"{'=' * width} {title} {'=' * width}"


def notify_if_empty():
    if not expenses:
        print("No expenses recorded yet.")
        return True
    return False


def display_expense(expense_id, info):
    print(f"ID: {expense_id}")
    print(f"Category: {info['category']}")
    print(f"Amount: £{info['amount']:,.2f}")
    print(f"Date: {info['date']}")
    print(f"Description: {info['description']}")
    print("-----------------")


def get_unique_id():
    while True:
        expense_id = input("Enter Expense ID: ").strip()
        if not expense_id:
            print("Expense ID cannot be empty.")
            continue
        if expense_id in expenses:
            print("Expense ID already exists.")
            continue
        return expense_id


def get_valid_category():
    while True:
        category = input("Enter Category: ").strip()
        if not category:
            print("Category cannot be empty.")
            continue
        return category


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue
        return amount


def get_valid_date():
    while True:
        expense_date = input(f"Enter Date ({DATE_FORMAT}): ").strip()
        try:
            datetime.strptime(expense_date, DATE_FORMAT)
        except ValueError:
            print(f"Date must be in {DATE_FORMAT} format.")
            continue
        return expense_date


def add_expense():
    expense_id = get_unique_id()
    category = get_valid_category()
    amount = get_valid_amount()
    expense_date = get_valid_date()
    description = input("Enter Description: ").strip()

    expenses[expense_id] = {
        "category": category,
        "amount": amount,
        "date": expense_date,
        "description": description,
    }
    save_expenses()
    print("Expense added successfully.")


def view_expenses():
    if notify_if_empty():
        return
    for expense_id, info in expenses.items():
        display_expense(expense_id, info)


def search_by_id():
    if notify_if_empty():
        return
    expense_id = input("Enter Expense ID: ").strip()
    if expense_id in expenses:
        display_expense(expense_id, expenses[expense_id])
    else:
        print("Expense not found.")


def search_by_category():
    if notify_if_empty():
        return
    query = input("Enter Category: ").strip().lower()
    found = False
    for expense_id, info in expenses.items():
        if info["category"].lower() == query:
            display_expense(expense_id, info)
            found = True
    if not found:
        print("No expenses found in this category.")


def search_expense():
    while True:
        choice = input(
            f"\n{format_header('Search Expense')}\n"
            "1. Search by ID\n"
            "2. Search by Category\n"
            "3. Return\n\n"
            "Enter your choice: "
        )

        if choice == "1":
            search_by_id()
        elif choice == "2":
            search_by_category()
        elif choice == "3":
            break
        else:
            print("Invalid Choice. Please pick 1-3.")


def delete_expense():
    if notify_if_empty():
        return
    expense_id = input("Enter Expense ID to delete: ").strip()
    if expense_id in expenses:
        del expenses[expense_id]
        save_expenses()
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")


def get_month_key(expense_date):
    return datetime.strptime(expense_date, DATE_FORMAT).strftime("%B %Y")


def get_monthly_totals():
    totals = {}
    for info in expenses.values():
        month = get_month_key(info["date"])
        totals[month] = totals.get(month, 0) + info["amount"]
    return totals


def monthly_summary():
    if notify_if_empty():
        return
    totals = get_monthly_totals()
    for month, total in sorted(totals.items(), key=lambda item: datetime.strptime(item[0], "%B %Y")):
        print(f"{month} : £{total:,.2f}")


def get_category_totals():
    totals = {}
    for info in expenses.values():
        totals[info["category"]] = totals.get(info["category"], 0) + info["amount"]
    return totals


def category_summary():
    if notify_if_empty():
        return
    totals = get_category_totals()
    for category, total in sorted(totals.items()):
        print(f"{category} : £{total:,.2f}")


def export_report():
    if notify_if_empty():
        return

    total_spending = sum(info["amount"] for info in expenses.values())
    highest_id = max(expenses, key=lambda i: expenses[i]["amount"])
    highest_info = expenses[highest_id]
    category_totals = get_category_totals()

    lines = []
    lines.append(format_header("EXPENSE REPORT", 10))
    lines.append("")
    lines.append("Generated On:")
    lines.append(datetime.now().strftime(DATE_FORMAT))
    lines.append("")
    lines.append("Total Spending:")
    lines.append(f"£{total_spending:,.2f}")
    lines.append("")
    lines.append("Highest Expense:")
    lines.append(f"{highest_id} - {highest_info['category']} - £{highest_info['amount']:,.2f} ({highest_info['date']})")
    lines.append("")
    lines.append("Total Expenses:")
    lines.append(str(len(expenses)))
    lines.append("")
    lines.append("Category Summary")
    lines.append("")
    for category, total in sorted(category_totals.items()):
        lines.append(f"{category} : £{total:,.2f}")
    lines.append("")
    lines.append("Complete Expense List")
    lines.append("")
    for expense_id, info in expenses.items():
        lines.append(f"ID: {expense_id}")
        lines.append(f"Category: {info['category']}")
        lines.append(f"Amount: £{info['amount']:,.2f}")
        lines.append(f"Date: {info['date']}")
        lines.append(f"Description: {info['description']}")
        lines.append("--------------------------------")
        lines.append("")

    report_text = "\n".join(lines)

    with open(REPORT_FILE, "w") as file:
        file.write(report_text)

    print(report_text)
    print("\nReport saved to expense_report.txt")


while True:
    choice = input(
        f"\n{format_header('Expense Tracker')}\n"
        "1. Add Expense\n"
        "2. View Expenses\n"
        "3. Search Expense\n"
        "4. Delete Expense\n"
        "5. Monthly Summary\n"
        "6. Category Summary\n"
        "7. Export Report\n"
        "8. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        monthly_summary()
    elif choice == "6":
        category_summary()
    elif choice == "7":
        export_report()
    elif choice == "8":
        print("Thank you for using Expense Tracker.")
        break
    else:
        print("Invalid Choice. Please pick 1-8.")
