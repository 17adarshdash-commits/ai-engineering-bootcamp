"""
main.py - App entry point for the multi-file FastAPI structure demo.

Demonstrates splitting an app into:
    main.py     -> FastAPI app, mounts routers
    routers.py  -> API routes
    models.py   -> Pydantic models
    services.py -> Business logic

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI

from routers import router as items_router

app = FastAPI(
    title="API Structure Demo",
    description="Demonstrates splitting a FastAPI app across main/routers/models/services.",
    version="1.0.0",
)

app.include_router(items_router)
