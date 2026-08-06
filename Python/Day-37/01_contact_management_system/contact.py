"""
contact.py

Defines the Contact class - a single contact record with an ID, name,
phone number, and email, plus conversion to/from a plain dict so it
can be (de)serialized to JSON.
"""


class Contact:
    """Represents a single contact."""

    def __init__(self, contact_id, name, phone, email):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        """Convert the Contact instance into a plain dictionary."""
        return {
            "contact_id": self.contact_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        """Build a Contact instance from a plain dictionary."""
        return cls(
            contact_id=data["contact_id"],
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
        )

    def __str__(self):
        return (
            f"ID: {self.contact_id} | Name: {self.name} | "
            f"Phone: {self.phone} | Email: {self.email}"
        )

    def __repr__(self):
        return (
            f"Contact(contact_id={self.contact_id!r}, name={self.name!r}, "
            f"phone={self.phone!r}, email={self.email!r})"
        )
