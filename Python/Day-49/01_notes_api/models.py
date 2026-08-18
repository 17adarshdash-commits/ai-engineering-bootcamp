"""models.py - Pydantic request/response shapes for the Notes API.

NoteCreate is what a client POSTs (id is server-assigned, so it's not
part of the input shape). Note is what the API stores and returns.
"""

from pydantic import BaseModel, field_validator


class NoteCreate(BaseModel):
    """Shape required to create a note."""

    title: str
    content: str
    category: str

    @field_validator("title", "content", "category")
    @classmethod
    def must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be empty")
        return value


class Note(NoteCreate):
    """Shape returned to clients - adds the server-assigned id."""

    id: int
