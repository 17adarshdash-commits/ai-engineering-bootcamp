"""
exceptions.py

Custom exceptions used across the expense tracker system.
"""


class ExpenseError(Exception):
    """Base exception for all expense-related errors."""


class DuplicateExpenseIDError(ExpenseError):
    """Raised when an expense ID already exists."""


class InvalidTitleError(ExpenseError):
    """Raised when an expense title is empty/blank."""


class InvalidCategoryError(ExpenseError):
    """Raised when an expense category is empty/blank."""


class InvalidAmountError(ExpenseError):
    """Raised when an amount is not a positive number."""


class InvalidDateError(ExpenseError):
    """Raised when a date is not in YYYY-MM-DD format."""


class ExpenseNotFoundError(ExpenseError):
    """Raised when an expense ID cannot be found."""
