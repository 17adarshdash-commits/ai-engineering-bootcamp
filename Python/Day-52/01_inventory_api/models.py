"""models.py - Pydantic request/response shapes for the Inventory API.

ProductCreate is what a client POSTs (id is server-assigned, so it's not
part of the input shape). ProductUpdate is what a client PUTs to replace
an existing record. Product is what the API stores and returns.
"""

from pydantic import BaseModel, field_validator


class ProductCreate(BaseModel):
    """Shape required to create a product."""

    name: str
    price: float
    quantity: int

    @field_validator("name")
    @classmethod
    def must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be empty")
        return value

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("price must be greater than 0")
        return value

    @field_validator("quantity")
    @classmethod
    def quantity_must_not_be_negative(cls, value: int) -> int:
        if value < 0:
            raise ValueError("quantity must not be negative")
        return value


class ProductUpdate(ProductCreate):
    """Shape required to replace an existing product (same fields as create)."""


class Product(ProductCreate):
    """Shape returned to clients - adds the server-assigned id."""

    id: int
