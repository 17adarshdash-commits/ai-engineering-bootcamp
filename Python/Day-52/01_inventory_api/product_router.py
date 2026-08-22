"""product_router.py - Product endpoints, isolated in their own APIRouter.

Mounted onto the app in main.py via app.include_router(product_router).
In-memory only - products live in a plain Python list for the lifetime
of the process, no SQLite today.
"""

from fastapi import APIRouter, HTTPException, status
from models import Product, ProductCreate, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])

products: list[Product] = [
    Product(id=1, name="Keyboard", price=999.0, quantity=25),
    Product(id=2, name="Mouse", price=499.0, quantity=40),
]
next_id = 3


def find_product(product_id: int) -> Product:
    """Return the product with product_id, or raise 404 if none exists."""
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found",
    )


@router.get("", response_model=list[Product])
def list_products() -> list[Product]:
    """Return all products."""
    return products


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    """Return a single product by id. 404 if it doesn't exist."""
    return find_product(product_id)


@router.post("", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate) -> Product:
    """Create a product and return it with its assigned id."""
    global next_id
    new_product = Product(id=next_id, **product.model_dump())
    products.append(new_product)
    next_id += 1
    return new_product


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate) -> Product:
    """Replace an existing product's fields. 404 if the id doesn't exist."""
    existing = find_product(product_id)
    updated = Product(id=existing.id, **product.model_dump())
    products[products.index(existing)] = updated
    return updated


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int) -> None:
    """Delete a product by id. 204 if removed, 404 if the id doesn't exist."""
    existing = find_product(product_id)
    products.remove(existing)
