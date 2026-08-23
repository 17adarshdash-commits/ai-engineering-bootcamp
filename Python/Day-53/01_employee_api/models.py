"""models.py - Pydantic request/response shapes for the Employee API.

EmployeeCreate is what a client POSTs (id is server-assigned, so it's
not part of the input shape). EmployeeUpdate is what a client PUTs to
replace an existing record. Employee is what the API stores and
returns.
"""

from pydantic import BaseModel, field_validator


class EmployeeCreate(BaseModel):
    """Shape required to create an employee."""

    name: str
    department: str
    salary: float

    @field_validator("name", "department")
    @classmethod
    def must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be empty")
        return value

    @field_validator("salary")
    @classmethod
    def salary_must_be_positive(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("salary must be greater than 0")
        return value


class EmployeeUpdate(EmployeeCreate):
    """Shape required to replace an existing employee (same fields as create)."""


class Employee(EmployeeCreate):
    """Shape returned to clients - adds the server-assigned id."""

    id: int
