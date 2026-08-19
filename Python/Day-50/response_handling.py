"""
response_handling.py - practicing path operations and response handling.

All in one file, in-memory only. Covers the four path operation
decorators and the different ways to shape a response (plain dict,
list of Pydantic models, and explicit status codes for create/delete).

Run with:
    uvicorn response_handling:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Student API",
    description="Practice API for path operations and response handling.",
    version="1.0.0",
)


class StudentCreate(BaseModel):
    """Shape required to create a student."""

    name: str
    department: str


class Student(StudentCreate):
    """Shape returned to clients - adds the server-assigned id."""

    id: int


students: list[Student] = [
    Student(id=1, name="Ava Chen", department="Computer Science"),
    Student(id=2, name="Ben Osei", department="Mathematics"),
]
next_id = 3


@app.get("/")
def read_root() -> dict:
    """Plain dict response - no response_model needed for a fixed shape."""
    return {"message": "Welcome to the Student API"}


@app.get("/students", response_model=list[Student])
def list_students() -> list[Student]:
    """Return the sample list of students."""
    return students


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate) -> Student:
    """Create a student and return it with its assigned id, as 201 Created."""
    global next_id
    new_student = Student(id=next_id, **student.model_dump())
    students.append(new_student)
    next_id += 1
    return new_student


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int) -> None:
    """Delete a student by id. 204 if removed, 404 if the id doesn't exist."""
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with id {student_id} not found",
    )
