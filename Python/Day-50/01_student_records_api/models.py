"""models.py - Pydantic request/response shapes for the Student Records API.

StudentCreate is what a client POSTs (id is server-assigned, so it's not
part of the input shape). StudentUpdate is what a client PUTs to replace
an existing record. Student is what the API stores and returns.
"""

from pydantic import BaseModel, field_validator


class StudentCreate(BaseModel):
    """Shape required to create a student."""

    name: str
    department: str
    cgpa: float

    @field_validator("name", "department")
    @classmethod
    def must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be empty")
        return value

    @field_validator("cgpa")
    @classmethod
    def must_be_in_range(cls, value: float) -> float:
        if not 0.0 <= value <= 10.0:
            raise ValueError("cgpa must be between 0.0 and 10.0")
        return value


class StudentUpdate(StudentCreate):
    """Shape required to replace an existing student (same fields as create)."""


class Student(StudentCreate):
    """Shape returned to clients - adds the server-assigned id."""

    id: int
