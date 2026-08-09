"""
account.py

Defines the Account class - a single bank account with an account number,
holder, balance, type, and opening date, plus conversion to/from a plain
dict so it can be (de)serialized to JSON.
"""

ACCOUNT_TYPES = ("Savings", "Current")


class Account:
    """Represents a single bank account."""

    def __init__(self, account_number, holder_name, balance, account_type, opening_date):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.account_type = account_type
        self.opening_date = opening_date

    def deposit(self, amount):
        """Add `amount` to the balance. Assumes `amount` has been validated."""
        self.balance += amount

    def withdraw(self, amount):
        """Subtract `amount` from the balance. Assumes `amount` has been validated."""
        self.balance -= amount

    def to_dict(self):
        """Convert the Account instance into a plain dictionary."""
        return {
            "account_number": self.account_number,
            "holder_name": self.holder_name,
            "balance": self.balance,
            "account_type": self.account_type,
            "opening_date": self.opening_date,
        }

    @classmethod
    def from_dict(cls, data):
        """Build an Account instance from a plain dictionary."""
        return cls(
            account_number=data["account_number"],
            holder_name=data["holder_name"],
            balance=data["balance"],
            account_type=data["account_type"],
            opening_date=data["opening_date"],
        )

    def __str__(self):
        return (
            f"Account No: {self.account_number} | Holder: {self.holder_name} | "
            f"Type: {self.account_type} | Balance: {self.balance:.2f} | "
            f"Opened: {self.opening_date}"
        )

    def __repr__(self):
        return (
            f"Account(account_number={self.account_number!r}, holder_name={self.holder_name!r}, "
            f"balance={self.balance!r}, account_type={self.account_type!r}, "
            f"opening_date={self.opening_date!r})"
        )
