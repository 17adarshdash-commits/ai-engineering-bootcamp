"""models.py - Domain-level types shared by schemas.py and crud.py.

Just the Priority enum for now - the "model" of what a task's priority
is allowed to be, independent of how it's validated at the API boundary
(schemas.py) or stored as a row (database.py/crud.py).
"""

from enum import Enum


class Priority(str, Enum):
    """A task's priority. Inherits str so it serializes as plain text."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
