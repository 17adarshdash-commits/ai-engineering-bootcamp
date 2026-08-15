"""
schemas.py - Response-envelope schemas, kept separate from the core Student
domain model in models.py.

Splitting these out means models.py stays focused on "what is a Student",
while schemas.py holds shapes that only exist for the API's response
contracts (list wrappers, error bodies).
"""

from typing import List

from pydantic import BaseModel

from models import Student


class StudentListResponse(BaseModel):
    """Envelope for GET /students - count alongside the list of students."""

    count: int
    students: List[Student]


class ErrorResponse(BaseModel):
    """Shape of FastAPI's HTTPException detail body, documented explicitly
    so it shows up in the OpenAPI schema for error responses."""

    detail: str
