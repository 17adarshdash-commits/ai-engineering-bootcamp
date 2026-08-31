"""
Pydantic schemas - the API-facing shapes.

Kept separate from the SQLAlchemy model in models.py: the schemas
describe what a request body must contain and what a response looks
like, while the model describes what the database table looks like.

UserCreate takes a plain `password` (this is what the client sends),
but UserOut never includes it - only the hash exists past registration,
and even that is never returned to a client.
"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    """Shape expected in the request body for POST /register."""

    name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserOut(BaseModel):
    """Shape returned to the client - never includes a password or hash."""

    id: int
    name: str
    email: EmailStr

    # Lets Pydantic build this model straight from a SQLAlchemy object
    # (user.id, user.name, ...) instead of requiring a dict.
    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    """Shape expected in the request body for POST /login."""

    email: EmailStr
    password: str


class Token(BaseModel):
    """Shape returned to the client after a successful login."""

    access_token: str
    token_type: str = "bearer"
