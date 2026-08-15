"""
models.py - Pydantic models describing a Student, used for request/response
validation.
"""

from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Student name, cannot be empty")
    age: int = Field(..., ge=16, le=100, description="Student age, must be between 16 and 100")
    course: str = Field(..., min_length=1, max_length=100, description="Enrolled course, cannot be empty")
    cgpa: float = Field(..., ge=0.0, le=10.0, description="CGPA, must be between 0.0 and 10.0")


class StudentCreate(StudentBase):
    """Fields required to create a new student - id is assigned by the database."""

    pass


class StudentUpdate(StudentBase):
    """All fields required on update - PUT replaces the whole resource."""

    pass


class Student(StudentBase):
    """Full student record as returned by the API, including its id."""

    id: int
