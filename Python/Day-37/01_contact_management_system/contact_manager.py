"""
contact_manager.py

Defines the ContactManager class - handles CRUD operations, search,
display, and JSON persistence for a collection of Contact objects.
"""

import json
import os

from contact import Contact
from exceptions import (
    DuplicateContactIDError,
    InvalidEmailError,
    InvalidNameError,
    InvalidPhoneError,
    ContactNotFoundError,
)


class ContactManager:
    """Manages a collection of Contact objects."""

    def __init__(self):
        self.contacts = {}  # contact_id -> Contact

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_name(name):
        if not name or not name.strip():
            raise InvalidNameError("Name cannot be empty.")

    @staticmethod
    def _validate_email(email):
        if not email or "@" not in email:
            raise InvalidEmailError("Email must contain '@'.")

    @staticmethod
    def _validate_phone(phone):
        if not phone or not str(phone).strip():
            raise InvalidPhoneError("Phone number cannot be empty.")

    # ------------------------------------------------------------------
    # CRUD operations
    # ------------------------------------------------------------------
    def add_contact(self, contact_id, name, phone, email):
        """Add a new contact after validating all fields."""
        if contact_id in self.contacts:
            raise DuplicateContactIDError(f"Contact ID '{contact_id}' already exists.")

        self._validate_name(name)
        self._validate_phone(phone)
        self._validate_email(email)

        contact = Contact(contact_id, name.strip(), str(phone).strip(), email.strip())
        self.contacts[contact_id] = contact
        return contact

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        """Update fields of an existing contact. Only provided fields change."""
        contact = self._get_contact_or_raise(contact_id)

        if name is not None:
            self._validate_name(name)
            contact.name = name.strip()

        if phone is not None:
            self._validate_phone(phone)
            contact.phone = str(phone).strip()

        if email is not None:
            self._validate_email(email)
            contact.email = email.strip()

        return contact

    def delete_contact(self, contact_id):
        """Delete a contact by ID."""
        self._get_contact_or_raise(contact_id)
        del self.contacts[contact_id]

    def search_contact(self, keyword):
        """Search contacts by ID, name, phone, or email (case-insensitive substring match)."""
        keyword = str(keyword).strip().lower()
        results = [
            contact
            for contact in self.contacts.values()
            if keyword in str(contact.contact_id).lower()
            or keyword in contact.name.lower()
            or keyword in contact.phone.lower()
            or keyword in contact.email.lower()
        ]
        return results

    def display_contacts(self):
        """Print all contacts to the console."""
        if not self.contacts:
            print("No contacts to display.")
            return

        for contact in self.contacts.values():
            print(contact)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def save_to_json(self, filepath):
        """Save all contacts to a JSON file."""
        data = [contact.to_dict() for contact in self.contacts.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filepath):
        """Load contacts from a JSON file, replacing the current collection."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: '{filepath}'")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.contacts = {}
        for item in data:
            contact = Contact.from_dict(item)
            self.contacts[contact.contact_id] = contact

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _get_contact_or_raise(self, contact_id):
        if contact_id not in self.contacts:
            raise ContactNotFoundError(f"Contact ID '{contact_id}' not found.")
        return self.contacts[contact_id]
