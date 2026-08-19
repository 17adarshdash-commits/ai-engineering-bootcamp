"""
main.py - Student Records API.

All in one file today, as intended - no database, students live in a
plain Python list for the lifetime of the process. Reinforces path
operations, response handling, and HTTPException without the overhead
of a modular/SQLite project like Day 48's task manager.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from fastapi import FastAPI, HTTPException, status
from models import Student, StudentCreate, StudentUpdate

app = FastAPI(
    title="Student Records API",
    description="A simple in-memory REST API for managing student records.",
    version="1.0.0",
)

students: list[Student] = [
    Student(id=1, name="Ava Chen", department="Computer Science", cgpa=8.7),
    Student(id=2, name="Ben Osei", department="Mathematics", cgpa=7.9),
]
next_id = 3


def find_student(student_id: int) -> Student:
    """Return the student with student_id, or raise 404 if none exists."""
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with id {student_id} not found",
    )


@app.get("/students", response_model=list[Student])
def list_students() -> list[Student]:
    """Return all students."""
    return students


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int) -> Student:
    """Return a single student by id. 404 if it doesn't exist."""
    return find_student(student_id)


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate) -> Student:
    """Create a student and return it with its assigned id."""
    global next_id
    new_student = Student(id=next_id, **student.model_dump())
    students.append(new_student)
    next_id += 1
    return new_student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate) -> Student:
    """Replace an existing student's fields. 404 if the id doesn't exist."""
    existing = find_student(student_id)
    updated = Student(id=existing.id, **student.model_dump())
    students[students.index(existing)] = updated
    return updated


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int) -> None:
    """Delete a student by id. 204 if removed, 404 if the id doesn't exist."""
    existing = find_student(student_id)
    students.remove(existing)
