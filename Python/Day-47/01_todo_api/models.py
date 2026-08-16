"""models.py - Pydantic schemas for the Todo API."""

from pydantic import BaseModel


class TodoCreate(BaseModel):
    """Shape required to create a todo. id is assigned by the server."""

    task: str
    completed: bool = False


class Todo(TodoCreate):
    """Shape returned to clients - adds the server-assigned id."""

    id: int
