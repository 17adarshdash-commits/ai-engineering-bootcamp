"""schemas.py - Pydantic request/response shapes for the Task Manager API.

TaskCreate is what a client POSTs (id is client-supplied so create can be
checked for duplicates). TaskUpdate is what a client PUTs - same shape,
since this is a full replace, not a partial patch. Task is what the API
returns.
"""

from pydantic import BaseModel, field_validator

from models import Priority


class TaskCreate(BaseModel):
    """Shape required to create a task."""

    id: int
    title: str
    description: str = ""
    priority: Priority
    completed: bool = False

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("title must not be empty")
        return value


class TaskUpdate(BaseModel):
    """Shape required to fully replace an existing task (id comes from the URL)."""

    title: str
    description: str = ""
    priority: Priority
    completed: bool = False

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("title must not be empty")
        return value


class Task(BaseModel):
    """Shape returned to clients."""

    id: int
    title: str
    description: str
    priority: Priority
    completed: bool
