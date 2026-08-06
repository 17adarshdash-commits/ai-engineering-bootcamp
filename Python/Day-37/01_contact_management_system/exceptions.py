"""
exceptions.py

Custom exceptions used across the contact management system.
"""


class ContactError(Exception):
    """Base exception for all contact-related errors."""


class DuplicateContactIDError(ContactError):
    """Raised when a contact ID already exists."""


class InvalidNameError(ContactError):
    """Raised when a contact name is empty/blank."""


class InvalidEmailError(ContactError):
    """Raised when an email address doesn't contain '@'."""


class InvalidPhoneError(ContactError):
    """Raised when a phone number is empty/blank."""


class ContactNotFoundError(ContactError):
    """Raised when a contact ID cannot be found."""
