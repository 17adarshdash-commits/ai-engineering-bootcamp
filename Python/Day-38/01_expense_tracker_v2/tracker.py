"""
tracker.py

Defines the ExpenseTracker class - handles CRUD operations, search,
display, totals, and JSON persistence for a collection of Expense objects.
"""

import json
import os
from datetime import datetime

from expense import Expense
from exceptions import (
    DuplicateExpenseIDError,
    InvalidTitleError,
    InvalidCategoryError,
    InvalidAmountError,
    InvalidDateError,
    ExpenseNotFoundError,
)

DATE_FORMAT = "%Y-%m-%d"


class ExpenseTracker:
    """Manages a collection of Expense objects."""

    def __init__(self):
        self.expenses = {}  # expense_id -> Expense

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_title(title):
        if not title or not title.strip():
            raise InvalidTitleError("Title cannot be empty.")

    @staticmethod
    def _validate_category(category):
        if not category or not category.strip():
            raise InvalidCategoryError("Category cannot be empty.")

    @staticmethod
    def _validate_amount(amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise InvalidAmountError("Amount must be a number.")
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than 0.")
        return amount

    @staticmethod
    def _validate_date(date):
        try:
            datetime.strptime(date, DATE_FORMAT)
        except (TypeError, ValueError):
            raise InvalidDateError(
                f"Date must be in YYYY-MM-DD format, got: '{date}'."
            )

    # ------------------------------------------------------------------
    # CRUD operations
    # ------------------------------------------------------------------
    def add_expense(self, expense_id, title, category, amount, date):
        """Add a new expense after validating all fields."""
        if expense_id in self.expenses:
            raise DuplicateExpenseIDError(f"Expense ID '{expense_id}' already exists.")

        self._validate_title(title)
        self._validate_category(category)
        amount = self._validate_amount(amount)
        self._validate_date(date)

        expense = Expense(expense_id, title.strip(), category.strip(), amount, date)
        self.expenses[expense_id] = expense
        return expense

    def update_expense(self, expense_id, title=None, category=None, amount=None, date=None):
        """Update fields of an existing expense. Only provided fields change."""
        expense = self._get_expense_or_raise(expense_id)

        if title is not None:
            self._validate_title(title)
            expense.title = title.strip()

        if category is not None:
            self._validate_category(category)
            expense.category = category.strip()

        if amount is not None:
            expense.amount = self._validate_amount(amount)

        if date is not None:
            self._validate_date(date)
            expense.date = date

        return expense

    def delete_expense(self, expense_id):
        """Delete an expense by ID."""
        self._get_expense_or_raise(expense_id)
        del self.expenses[expense_id]

    def search_expenses(self, keyword):
        """Search expenses by ID, title, category, or date (case-insensitive substring match)."""
        keyword = str(keyword).strip().lower()
        results = [
            expense
            for expense in self.expenses.values()
            if keyword in str(expense.expense_id).lower()
            or keyword in expense.title.lower()
            or keyword in expense.category.lower()
            or keyword in expense.date.lower()
        ]
        return results

    def display_expenses(self):
        """Print all expenses to the console."""
        if not self.expenses:
            print("No expenses to display.")
            return

        for expense in self.expenses.values():
            print(expense)

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------
    def total_spending(self):
        """Return the total amount spent across all expenses."""
        return sum(expense.amount for expense in self.expenses.values())

    def spending_by_category(self):
        """Return a dict mapping category -> total amount spent."""
        totals = {}
        for expense in self.expenses.values():
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount
        return totals

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def save_to_json(self, filepath):
        """Save all expenses to a JSON file."""
        data = [expense.to_dict() for expense in self.expenses.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filepath):
        """Load expenses from a JSON file, replacing the current collection."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: '{filepath}'")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.expenses = {}
        for item in data:
            expense = Expense.from_dict(item)
            self.expenses[expense.expense_id] = expense

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _get_expense_or_raise(self, expense_id):
        if expense_id not in self.expenses:
            raise ExpenseNotFoundError(f"Expense ID '{expense_id}' not found.")
        return self.expenses[expense_id]
