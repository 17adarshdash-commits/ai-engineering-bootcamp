"""
main.py - Student Management REST API V2.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

import sqlite3
from typing import List

from fastapi import Depends, FastAPI, status

import crud
from database import init_db
from dependencies import get_db, get_existing_student
from models import Student, StudentCreate, StudentUpdate
from schemas import StudentListResponse

app = FastAPI(
    title="Student Management API V2",
    description="A REST API for managing students, backed by SQLite, "
    "built with dependency injection and layered project structure.",
    version="2.0.0",
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/students", response_model=StudentListResponse)
def list_students(conn: sqlite3.Connection = Depends(get_db)) -> StudentListResponse:
    """Return all students."""
    students = crud.get_all_students(conn)
    return StudentListResponse(count=len(students), students=students)


@app.get("/students/{student_id}", response_model=Student)
def get_student(student: Student = Depends(get_existing_student)) -> Student:
    """Retrieve a single student by ID. 404 if the student doesn't exist."""
    return student


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(
    student: StudentCreate, conn: sqlite3.Connection = Depends(get_db)
) -> Student:
    """Create a new student. Field validation (name length, age range,
    course length, CGPA range) is enforced by Pydantic before this runs."""
    return crud.create_student(conn, student)


@app.put("/students/{student_id}", response_model=Student)
def update_student(
    student_update: StudentUpdate,
    existing: Student = Depends(get_existing_student),
    conn: sqlite3.Connection = Depends(get_db),
) -> Student:
    """Update an existing student. 404 if the student doesn't exist."""
    return crud.update_student(conn, existing.id, student_update)


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(
    existing: Student = Depends(get_existing_student),
    conn: sqlite3.Connection = Depends(get_db),
) -> None:
    """Delete a student. 404 if the student doesn't exist."""
    crud.delete_student(conn, existing.id)
