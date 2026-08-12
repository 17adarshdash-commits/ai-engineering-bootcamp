"""
member.py

Defines the Member dataclass - a single library member with an ID, name,
and email, plus conversion to/from a plain tuple so it can be
(de)serialized to/from a SQLite row.
"""

from dataclasses import dataclass


@dataclass
class Member:
    """Represents a single library member."""

    member_id: str
    name: str
    email: str

    def to_row(self):
        """Convert the Member instance into a tuple matching the members table's column order."""
        return (self.member_id, self.name, self.email)

    @classmethod
    def from_row(cls, row):
        """Build a Member instance from a SQLite row (member_id, name, email)."""
        member_id, name, email = row
        return cls(member_id=member_id, name=name, email=email)

    def __str__(self):
        return f"ID: {self.member_id} | {self.name} | {self.email}"
