"""
dependency_injection.py - Dependency Injection basics with FastAPI's Depends.

Run with:
    uvicorn dependency_injection:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

from fastapi import Depends, FastAPI

app = FastAPI(
    title="Dependency Injection Demo",
    description="Demonstrates injecting a shared dependency with Depends().",
)


def get_current_user() -> dict:
    """A dependency: FastAPI calls this and injects its return value into
    any route parameter declared as Depends(get_current_user).

    In a real app this would decode a token / look up a session; here it's
    hardcoded to keep the focus on the DI mechanism itself.
    """
    return {"username": "admin"}


@app.get("/")
def home(user: dict = Depends(get_current_user)) -> dict:
    """Root endpoint - greets the injected user."""
    return {"message": f"Hello, {user['username']}!"}


@app.get("/profile")
def profile(user: dict = Depends(get_current_user)) -> dict:
    """Return the injected user's profile information."""
    return {"user": user}
