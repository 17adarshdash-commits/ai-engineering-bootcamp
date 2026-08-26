"""
SQLAlchemy model(s) + Pydantic schemas.

The SQLAlchemy model (`User`) is the database-facing shape; the
Pydantic schemas are the API-facing shapes. Keeping them separate means
the API contract doesn't have to leak every internal DB detail.
"""

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    age = Column(Integer, nullable=False)


class UserCreate(BaseModel):
    """Shape expected in the request body for POST /users."""

    name: str
    email: str
    age: int


class UserOut(BaseModel):
    """Shape returned to the client - includes the generated id."""

    id: int
    name: str
    email: str
    age: int

    # Lets Pydantic build this model straight from a SQLAlchemy object
    # (user.id, user.name, ...) instead of requiring a dict.
    model_config = ConfigDict(from_attributes=True)
