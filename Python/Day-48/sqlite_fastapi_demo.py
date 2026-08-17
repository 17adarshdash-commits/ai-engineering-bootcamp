"""
sqlite_fastapi_demo.py - FastAPI connected to SQLite instead of a list.

Students are stored in a real SQLite database file (students.db, created
next to this script on first run) rather than in-memory. The point is to
see the three pieces that change versus a list-backed API: opening a
short-lived connection per request, running parameterized SQL, and
mapping rows back into Pydantic models for the response.

Run with:
    uvicorn sqlite_fastapi_demo:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

import sqlite3
from pathlib import Path

from fastapi import FastAPI, status
from pydantic import BaseModel

DB_PATH = Path(__file__).parent / "students.db"

app = FastAPI(
    title="SQLite Students Demo",
    description="Students stored in SQLite instead of a Python list.",
    version="1.0.0",
)


class StudentCreate(BaseModel):
    """Shape required to create a student. id is assigned by SQLite."""

    name: str
    course: str


class Student(StudentCreate):
    """Shape returned to clients - adds the database-assigned id."""

    id: int


def get_connection() -> sqlite3.Connection:
    """Open a short-lived connection with dict-like row access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the students table if it doesn't exist yet."""
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.get("/students", response_model=list[Student])
def get_students() -> list[Student]:
    """Return every student stored in SQLite."""
    conn = get_connection()
    rows = conn.execute("SELECT id, name, course FROM students").fetchall()
    conn.close()
    return [Student(**dict(row)) for row in rows]


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate) -> Student:
    """Insert a new student and return it with its assigned id."""
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO students (name, course) VALUES (?, ?)",
        (student.name, student.course),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return Student(id=new_id, name=student.name, course=student.course)
