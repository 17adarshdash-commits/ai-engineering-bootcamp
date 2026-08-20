"""models.py - Pydantic request/response shapes for the Course API.

CourseCreate is what a client POSTs (id is server-assigned, so it's not
part of the input shape). CourseUpdate is what a client PUTs to replace
an existing record. Course is what the API stores and returns.
"""

from pydantic import BaseModel, field_validator


class CourseCreate(BaseModel):
    """Shape required to create a course."""

    name: str
    instructor: str
    credits: int

    @field_validator("name", "instructor")
    @classmethod
    def must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be empty")
        return value

    @field_validator("credits")
    @classmethod
    def must_be_in_range(cls, value: int) -> int:
        if not 1 <= value <= 6:
            raise ValueError("credits must be between 1 and 6")
        return value


class CourseUpdate(CourseCreate):
    """Shape required to replace an existing course (same fields as create)."""


class Course(CourseCreate):
    """Shape returned to clients - adds the server-assigned id."""

    id: int
