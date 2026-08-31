"""
Pydantic schemas - the API-facing shapes.

Kept separate from the SQLAlchemy models in models.py: the schemas
describe what a request body must contain and what a response looks
like, while the models describe what the database table looks like.
"""

from pydantic import BaseModel, ConfigDict


# ---- User ----

class UserCreate(BaseModel):
    """Shape expected in the request body for POST /users."""

    name: str
    email: str


class UserOut(BaseModel):
    """Shape returned to the client - includes the generated id."""

    id: int
    name: str
    email: str

    # Lets Pydantic build this model straight from a SQLAlchemy object
    # (user.id, user.name, ...) instead of requiring a dict.
    model_config = ConfigDict(from_attributes=True)


# ---- Post ----

class PostCreate(BaseModel):
    """Shape expected in the request body for POST /posts."""

    title: str
    content: str
    user_id: int


class PostUpdate(BaseModel):
    """Shape expected in the request body for PUT /posts/{id}."""

    title: str
    content: str


class PostOut(BaseModel):
    """Shape returned to the client - includes the generated id."""

    id: int
    title: str
    content: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)
