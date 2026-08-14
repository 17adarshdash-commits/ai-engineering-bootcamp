"""
Day 45 - Practice 2: Path parameters and query parameters.

Run with:
    uvicorn path_query_parameters:app --reload

Examples:
    GET /students/5
        -> {"student_id": 5}

    GET /search?name=Alice&course=Math
        -> {"name": "Alice", "course": "Math"}

    GET /search
        -> {"name": None, "course": None}
"""

from typing import Optional

from fastapi import FastAPI

app = FastAPI(title="Path & Query Parameters Practice")


@app.get("/students/{student_id}")
def get_student(student_id: int) -> dict:
    """Path parameter example - student_id comes straight from the URL path."""
    return {"student_id": student_id}


@app.get("/search")
def search(name: Optional[str] = None, course: Optional[str] = None) -> dict:
    """Query parameter example - both are optional filters on the search."""
    return {"name": name, "course": course}
