"""
expense.py

Defines the Expense class - a single expense record with an ID, title,
category, amount, and date, plus conversion to/from a plain dict so it
can be (de)serialized to JSON.
"""


class Expense:
    """Represents a single expense."""

    def __init__(self, expense_id, title, category, amount, date):
        self.expense_id = expense_id
        self.title = title
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self):
        """Convert the Expense instance into a plain dictionary."""
        return {
            "expense_id": self.expense_id,
            "title": self.title,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        """Build an Expense instance from a plain dictionary."""
        return cls(
            expense_id=data["expense_id"],
            title=data["title"],
            category=data["category"],
            amount=data["amount"],
            date=data["date"],
        )

    def __str__(self):
        return (
            f"ID: {self.expense_id} | Title: {self.title} | "
            f"Category: {self.category} | Amount: {self.amount:.2f} | "
            f"Date: {self.date}"
        )

    def __repr__(self):
        return (
            f"Expense(expense_id={self.expense_id!r}, title={self.title!r}, "
            f"category={self.category!r}, amount={self.amount!r}, date={self.date!r})"
        )
