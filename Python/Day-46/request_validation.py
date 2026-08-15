"""
request_validation.py - Request body validation with Pydantic Field().

Run with:
    uvicorn request_validation:app --reload

Docs:
    http://127.0.0.1:8000/docs

Try invalid inputs in Swagger to see FastAPI's automatic 422 responses, e.g.:
    {"id": 1, "name": "ab", "price": 10.0, "quantity": 5}       -> name too short
    {"id": 1, "name": "Widget", "price": -5, "quantity": 5}     -> price must be > 0
    {"id": 1, "name": "Widget", "price": 10.0, "quantity": -1}  -> quantity must be >= 0
"""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Request Validation Demo",
    description="Demonstrates Pydantic Field() constraints for request validation.",
)


class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50, description="Product name, 3-50 chars")
    price: float = Field(..., gt=0, description="Price, must be greater than 0")
    quantity: int = Field(..., ge=0, description="Quantity in stock, must be >= 0")


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: Product) -> Product:
    """Validate and return the submitted product.

    All the validation here (length/range checks) is enforced by Pydantic
    before this function body even runs - invalid input never reaches it,
    FastAPI responds with 422 automatically.
    """
    return product
