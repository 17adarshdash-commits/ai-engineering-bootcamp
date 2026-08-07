"""
main.py

Command-line interface for the Expense Tracker V2.
"""

from tracker import ExpenseTracker
from exceptions import ExpenseError

DATA_FILE = "expenses.json"

MENU = """
========== Expense Tracker V2 ==========
1. Add Expense
2. Update Expense
3. Delete Expense
4. Search Expenses
5. Display All Expenses
6. Total Spending
7. Spending by Category
8. Save Expenses to JSON
9. Load Expenses from JSON
10. Exit
==========================================
"""


def add_expense(tracker):
    expense_id = input("Enter expense ID: ").strip()
    title = input("Enter title: ").strip()
    category = input("Enter category: ").strip()
    amount = input("Enter amount: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        tracker.add_expense(expense_id, title, category, amount, date)
        print("Expense added successfully.")
    except ExpenseError as e:
        print(f"Error: {e}")


def update_expense(tracker):
    expense_id = input("Enter expense ID to update: ").strip()
    print("Leave a field blank to keep it unchanged.")
    title = input("New title: ").strip() or None
    category = input("New category: ").strip() or None
    amount = input("New amount: ").strip() or None
    date = input("New date (YYYY-MM-DD): ").strip() or None

    try:
        tracker.update_expense(
            expense_id, title=title, category=category, amount=amount, date=date
        )
        print("Expense updated successfully.")
    except ExpenseError as e:
        print(f"Error: {e}")


def delete_expense(tracker):
    expense_id = input("Enter expense ID to delete: ").strip()
    try:
        tracker.delete_expense(expense_id)
        print("Expense deleted successfully.")
    except ExpenseError as e:
        print(f"Error: {e}")


def search_expenses(tracker):
    keyword = input("Enter search keyword (ID/title/category/date): ").strip()
    results = tracker.search_expenses(keyword)
    if not results:
        print("No matching expenses found.")
        return

    for expense in results:
        print(expense)


def display_expenses(tracker):
    tracker.display_expenses()


def total_spending(tracker):
    print(f"Total spending: {tracker.total_spending():.2f}")


def spending_by_category(tracker):
    totals = tracker.spending_by_category()
    if not totals:
        print("No expenses to summarize.")
        return

    for category, total in totals.items():
        print(f"{category}: {total:.2f}")


def save_expenses(tracker):
    filepath = input(f"Enter filepath to save [{DATA_FILE}]: ").strip() or DATA_FILE
    tracker.save_to_json(filepath)
    print(f"Expenses saved to '{filepath}'.")


def load_expenses(tracker):
    filepath = input(f"Enter filepath to load [{DATA_FILE}]: ").strip() or DATA_FILE
    try:
        tracker.load_from_json(filepath)
        print(f"Expenses loaded from '{filepath}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def main():
    tracker = ExpenseTracker()

    actions = {
        "1": add_expense,
        "2": update_expense,
        "3": delete_expense,
        "4": search_expenses,
        "5": display_expenses,
        "6": total_spending,
        "7": spending_by_category,
        "8": save_expenses,
        "9": load_expenses,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "10":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(tracker)


if __name__ == "__main__":
    main()
