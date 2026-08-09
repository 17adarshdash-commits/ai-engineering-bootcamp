"""
exceptions.py

Custom exceptions used across the banking system.
"""


class BankError(Exception):
    """Base exception for all banking-related errors."""


class DuplicateAccountError(BankError):
    """Raised when an account number already exists."""


class InvalidAccountHolderError(BankError):
    """Raised when an account holder name is empty/blank."""


class InvalidAccountTypeError(BankError):
    """Raised when an account type is not Savings or Current."""


class InvalidAmountError(BankError):
    """Raised when a deposit/withdraw/transfer amount is not positive."""


class InsufficientFundsError(BankError):
    """Raised when a withdrawal or transfer exceeds the available balance."""


class InvalidOpeningDateError(BankError):
    """Raised when an opening date is not in YYYY-MM-DD format."""


class AccountNotFoundError(BankError):
    """Raised when an account number cannot be found."""
