"""
dependencies_demo.py - Reusing a single dependency across multiple routes.

get_current_user is declared once and injected into every route below via
Depends(get_current_user). Each endpoint reuses the same dependency instead
of re-fetching/hardcoding the user itself.

Run with:
    uvicorn dependencies_demo:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

from fastapi import Depends, FastAPI

app = FastAPI(
    title="Dependencies Demo",
    description="Demonstrates reusing one Depends() dependency across routes.",
    version="1.0.0",
)


def get_current_user() -> dict:
    """A dependency: FastAPI calls this and injects its return value into
    any route parameter declared as Depends(get_current_user).

    In a real app this would decode a token / look up a session; here it's
    hardcoded to keep the focus on the DI mechanism itself.
    """
    return {"username": "adarsh", "role": "student"}


@app.get("/")
def home(user: dict = Depends(get_current_user)) -> dict:
    """Root endpoint - greets the injected user."""
    return {"message": f"Welcome, {user['username']}!"}


@app.get("/profile")
def profile(user: dict = Depends(get_current_user)) -> dict:
    """Return the injected user's profile information."""
    return {"user": user}


@app.get("/dashboard")
def dashboard(user: dict = Depends(get_current_user)) -> dict:
    """Return a dashboard payload personalized with the injected user."""
    return {
        "username": user["username"],
        "role": user["role"],
        "message": f"Here's your dashboard, {user['username']}.",
    }
