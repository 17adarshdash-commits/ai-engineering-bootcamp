"""
Day 45 - Practice 1: Your first FastAPI app.

Run with:
    uvicorn first_fastapi_app:app --reload

Then visit:
    http://127.0.0.1:8000/            -> {"message": "Hello FastAPI"}
    http://127.0.0.1:8000/about       -> API info
    http://127.0.0.1:8000/health      -> {"status": "healthy"}
    http://127.0.0.1:8000/docs        -> Swagger UI
    http://127.0.0.1:8000/redoc       -> ReDoc
"""

from fastapi import FastAPI

app = FastAPI(
    title="First FastAPI App",
    description="A minimal FastAPI app used to learn the basics.",
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict:
    """Root endpoint - simple greeting."""
    return {"message": "Hello FastAPI"}


@app.get("/about")
def about() -> dict:
    """Information about this API."""
    return {
        "name": "First FastAPI App",
        "version": "1.0.0",
        "description": "A learning project for Day 45 of the AI Engineering Bootcamp.",
        "author": "Adarsh Dash",
    }


@app.get("/health")
def health_check() -> dict:
    """Simple health check endpoint."""
    return {"status": "healthy"}
