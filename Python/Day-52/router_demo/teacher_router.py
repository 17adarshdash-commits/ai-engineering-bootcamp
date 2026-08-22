"""teacher_router.py - Teacher endpoints, isolated in their own APIRouter.

Mounted onto the app in main.py via app.include_router(teacher_router).
Mirrors student_router.py's shape so the two resources stay symmetric.
"""

from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/teachers", tags=["Teachers"])

teachers = [
    {"id": 1, "name": "Dr. Rao"},
    {"id": 2, "name": "Dr. Iyer"},
    {"id": 3, "name": "Dr. Nair"},
]


@router.get("")
def list_teachers() -> list[dict]:
    """Return every teacher."""
    return teachers


@router.get("/{teacher_id}")
def get_teacher(teacher_id: int) -> dict:
    """Return a single teacher by id. 404 if it doesn't exist."""
    for teacher in teachers:
        if teacher["id"] == teacher_id:
            return teacher
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Teacher with id {teacher_id} not found",
    )
