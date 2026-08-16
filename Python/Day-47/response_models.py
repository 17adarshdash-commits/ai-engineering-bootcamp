"""
response_models.py - GET /student using a Pydantic response model.

Run with:
    uvicorn response_models:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc

Try it: GET /student -> {"id": 1, "name": "Alice", "course": "AI"}

The handler returns a plain dict, but `response_model=Student` validates and
serializes it against the Student schema before it's sent - any field not
declared on Student would be dropped, and a missing/mistyped field would
raise a server-side error instead of shipping a malformed response.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Response Models Demo",
    description="Demonstrates response_model= for shaping and validating API output.",
)


class Student(BaseModel):
    id: int
    name: str
    course: str


@app.get("/student", response_model=Student)
def get_student() -> dict:
    """Return a single hardcoded student, validated against the Student model."""
    return {"id": 1, "name": "Alice", "course": "AI"}
