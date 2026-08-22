"""student_router.py - Student endpoints, isolated in their own APIRouter.

Mounted onto the app in main.py via app.include_router(student_router).
Nothing in here needs to know how it's mounted, or what other routers
exist - it only owns the "/students" resource.
"""

from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/students", tags=["Students"])

students = [
    {"id": 1, "name": "Adarsh"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Rahul"},
]


@router.get("")
def list_students() -> list[dict]:
    """Return every student."""
    return students


@router.get("/{student_id}")
def get_student(student_id: int) -> dict:
    """Return a single student by id. 404 if it doesn't exist."""
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with id {student_id} not found",
    )
