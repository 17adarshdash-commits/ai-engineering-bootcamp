"""
bank.py

Defines the Bank class - handles account creation, deposits, withdrawals,
transfers, search, display, and JSON persistence for a collection of
Account objects.
"""

import json
import os
from datetime import datetime

from account import Account, ACCOUNT_TYPES
from exceptions import (
    DuplicateAccountError,
    InvalidAccountHolderError,
    InvalidAccountTypeError,
    InvalidAmountError,
    InsufficientFundsError,
    InvalidOpeningDateError,
    AccountNotFoundError,
)

DATE_FORMAT = "%Y-%m-%d"


class Bank:
    """Manages a collection of Account objects."""

    def __init__(self):
        self.accounts = {}  # account_number -> Account

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_holder_name(holder_name):
        if not holder_name or not holder_name.strip():
            raise InvalidAccountHolderError("Account holder name cannot be empty.")

    @staticmethod
    def _validate_account_type(account_type):
        if account_type not in ACCOUNT_TYPES:
            raise InvalidAccountTypeError(
                f"Account type must be one of {ACCOUNT_TYPES}, got: '{account_type}'."
            )

    @staticmethod
    def _validate_opening_date(opening_date):
        try:
            datetime.strptime(opening_date, DATE_FORMAT)
        except (TypeError, ValueError):
            raise InvalidOpeningDateError(
                f"Opening date must be in YYYY-MM-DD format, got: '{opening_date}'."
            )

    @staticmethod
    def _validate_amount(amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise InvalidAmountError("Amount must be a number.")
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than 0.")
        return amount

    # ------------------------------------------------------------------
    # Account creation
    # ------------------------------------------------------------------
    def create_account(
        self, account_number, holder_name, account_type, opening_date, balance=0
    ):
        """Create a new account after validating all fields."""
        if account_number in self.accounts:
            raise DuplicateAccountError(f"Account number '{account_number}' already exists.")

        self._validate_holder_name(holder_name)
        self._validate_account_type(account_type)
        self._validate_opening_date(opening_date)

        try:
            balance = float(balance)
        except (TypeError, ValueError):
            raise InvalidAmountError("Opening balance must be a number.")
        if balance < 0:
            raise InvalidAmountError("Opening balance cannot be negative.")

        account = Account(
            account_number,
            holder_name.strip(),
            balance,
            account_type,
            opening_date,
        )
        self.accounts[account_number] = account
        return account

    # ------------------------------------------------------------------
    # Transactions
    # ------------------------------------------------------------------
    def deposit(self, account_number, amount):
        """Deposit a positive amount into an account."""
        account = self._get_account_or_raise(account_number)
        amount = self._validate_amount(amount)
        account.deposit(amount)
        return account

    def withdraw(self, account_number, amount):
        """Withdraw a positive amount from an account, up to its balance."""
        account = self._get_account_or_raise(account_number)
        amount = self._validate_amount(amount)
        if amount > account.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount:.2f}: balance is only {account.balance:.2f}."
            )
        account.withdraw(amount)
        return account

    def transfer(self, from_account_number, to_account_number, amount):
        """Transfer a positive amount from one account to another."""
        from_account = self._get_account_or_raise(from_account_number)
        to_account = self._get_account_or_raise(to_account_number)
        amount = self._validate_amount(amount)

        if from_account_number == to_account_number:
            raise InvalidAmountError("Cannot transfer to the same account.")
        if amount > from_account.balance:
            raise InsufficientFundsError(
                f"Cannot transfer {amount:.2f}: balance is only {from_account.balance:.2f}."
            )

        from_account.withdraw(amount)
        to_account.deposit(amount)
        return from_account, to_account

    # ------------------------------------------------------------------
    # Search / display
    # ------------------------------------------------------------------
    def search_account(self, keyword):
        """Search accounts by account number, holder name, or type (case-insensitive substring match)."""
        keyword = str(keyword).strip().lower()
        results = [
            account
            for account in self.accounts.values()
            if keyword in str(account.account_number).lower()
            or keyword in account.holder_name.lower()
            or keyword in account.account_type.lower()
        ]
        return results

    def display_accounts(self):
        """Print all accounts to the console."""
        if not self.accounts:
            print("No accounts to display.")
            return

        for account in self.accounts.values():
            print(account)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def save_to_json(self, filepath):
        """Save all accounts to a JSON file."""
        data = [account.to_dict() for account in self.accounts.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filepath):
        """Load accounts from a JSON file, replacing the current collection."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: '{filepath}'")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.accounts = {}
        for item in data:
            account = Account.from_dict(item)
            self.accounts[account.account_number] = account

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _get_account_or_raise(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError(f"Account number '{account_number}' not found.")
        return self.accounts[account_number]
