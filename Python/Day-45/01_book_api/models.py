"""
models.py - Pydantic models used for request/response validation.
"""

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, description="Book title, cannot be empty")
    author: str = Field(..., min_length=1, description="Book author, cannot be empty")
    category: str = Field(default="", description="Book category/genre")
    price: float = Field(..., gt=0, description="Price, must be greater than 0")
    stock: int = Field(..., ge=0, description="Stock quantity, must be >= 0")


class BookCreate(BookBase):
    id: int = Field(..., description="Unique book ID, must not already exist")


class BookUpdate(BookBase):
    """All fields required on update - PUT replaces the whole resource."""

    pass


class Book(BookBase):
    id: int
