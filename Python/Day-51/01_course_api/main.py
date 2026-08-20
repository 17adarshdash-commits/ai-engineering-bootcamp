"""
main.py - Course API.

In-memory only - courses live in a plain Python list for the lifetime of
the process, no SQLite today. Focus is FastAPI project structure and
dependency injection: get_current_user is declared once and reused by
GET /courses to demonstrate Depends() outside of a pure auth example.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from fastapi import Depends, FastAPI, HTTPException, status
from models import Course, CourseCreate, CourseUpdate

app = FastAPI(
    title="Course API",
    description="A simple in-memory REST API for managing courses.",
    version="1.0.0",
)

courses: list[Course] = [
    Course(id=1, name="Data Structures", instructor="Dr. Rao", credits=4),
    Course(id=2, name="Operating Systems", instructor="Dr. Iyer", credits=3),
]
next_id = 3


def get_current_user() -> dict:
    """A dependency: FastAPI calls this and injects its return value into
    any route parameter declared as Depends(get_current_user).

    In a real app this would decode a token / look up a session; here it's
    hardcoded to keep the focus on the DI mechanism itself.
    """
    return {"username": "adarsh", "role": "student"}


def find_course(course_id: int) -> Course:
    """Return the course with course_id, or raise 404 if none exists."""
    for course in courses:
        if course.id == course_id:
            return course
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Course with id {course_id} not found",
    )


@app.get("/courses", response_model=list[Course])
def list_courses(user: dict = Depends(get_current_user)) -> list[Course]:
    """Return all courses. Requires the injected current user."""
    return courses


@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int) -> Course:
    """Return a single course by id. 404 if it doesn't exist."""
    return find_course(course_id)


@app.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate) -> Course:
    """Create a course and return it with its assigned id."""
    global next_id
    new_course = Course(id=next_id, **course.model_dump())
    courses.append(new_course)
    next_id += 1
    return new_course


@app.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, course: CourseUpdate) -> Course:
    """Replace an existing course's fields. 404 if the id doesn't exist."""
    existing = find_course(course_id)
    updated = Course(id=existing.id, **course.model_dump())
    courses[courses.index(existing)] = updated
    return updated


@app.delete("/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int) -> None:
    """Delete a course by id. 204 if removed, 404 if the id doesn't exist."""
    existing = find_course(course_id)
    courses.remove(existing)
