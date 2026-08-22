"""main.py - Inventory API.

Stays minimal on purpose: create the app, include the router, done. All
product logic lives in product_router.py, the resource module it's
mounted from.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from fastapi import FastAPI
from product_router import router as product_router

app = FastAPI(
    title="Inventory API",
    description="A simple in-memory REST API for managing products.",
    version="1.0.0",
)

app.include_router(product_router)
