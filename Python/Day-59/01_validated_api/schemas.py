"""
Pydantic schemas - the API-facing shapes.

Kept separate from the SQLAlchemy models in models.py: the schemas
describe what a request body must contain and what a response looks
like, while the models describe what the database table looks like.

Day 59 adds real validation on top of Day 58's plain `str`/`int`
fields:
    - `EmailStr` rejects anything that isn't a real email shape
      ("not-an-email" fails instead of being stored as-is).
    - `Field(..., min_length=1)` rejects empty/blank names.
    - `Field(..., gt=0, le=150)` keeps age inside a sane range.
    - Sending the wrong *type* (e.g. `"name": 123` or
      `"age": "hello"`) is rejected automatically by Pydantic before
      the request handler ever runs - that's the 422 response.
"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ---- User ----

class UserCreate(BaseModel):
    """Shape expected in the request body for POST /users."""

    name: str = Field(..., min_length=1, description="Required, non-empty")
    email: EmailStr
    age: int = Field(..., gt=0, le=150)


class UserOut(BaseModel):
    """Shape returned to the client - includes the generated id."""

    id: int
    name: str
    email: EmailStr
    age: int

    # Lets Pydantic build this model straight from a SQLAlchemy object
    # (user.id, user.name, ...) instead of requiring a dict.
    model_config = ConfigDict(from_attributes=True)


# ---- Post ----

class PostCreate(BaseModel):
    """Shape expected in the request body for POST /posts."""

    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    user_id: int


class PostUpdate(BaseModel):
    """Shape expected in the request body for PUT /posts/{id}."""

    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


class PostOut(BaseModel):
    """Shape returned to the client - includes the generated id."""

    id: int
    title: str
    content: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)
