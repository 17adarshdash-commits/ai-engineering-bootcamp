"""
SQLAlchemy model(s) + Pydantic schemas.

The SQLAlchemy model (`Student`) is the database-facing shape; the
Pydantic schemas are the API-facing shapes. Keeping them separate means
the API contract doesn't have to leak every internal DB detail.
"""

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Float, Integer, String

from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    cgpa = Column(Float, nullable=False)


class StudentCreate(BaseModel):
    """Shape expected in the request body for POST /students."""

    name: str
    department: str
    cgpa: float


class StudentOut(BaseModel):
    """Shape returned to the client - includes the generated id."""

    id: int
    name: str
    department: str
    cgpa: float

    # Lets Pydantic build this model straight from a SQLAlchemy object
    # (student.id, student.name, ...) instead of requiring a dict.
    model_config = ConfigDict(from_attributes=True)
