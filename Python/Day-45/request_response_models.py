"""
Day 45 - Practice 3: Pydantic request/response models.

Run with:
    uvicorn request_response_models:app --reload

Examples:
    POST /students
        body: {"id": 1, "name": "Alice", "age": 20, "course": "Math"}
        -> returns the created student

    GET /students
        -> returns a list of sample students
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Request & Response Models Practice")


class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str


# In-memory store, pre-seeded with sample students so GET /students has data
# even before any POST requests are made.
students: list[Student] = [
    Student(id=1, name="Alice", age=20, course="Math"),
    Student(id=2, name="Bob", age=22, course="Physics"),
    Student(id=3, name="Charlie", age=21, course="Computer Science"),
]


@app.post("/students", response_model=Student)
def create_student(student: Student) -> Student:
    """Create a new student. FastAPI validates the body against Student automatically."""
    students.append(student)
    return student


@app.get("/students", response_model=list[Student])
def list_students() -> list[Student]:
    """Return the list of students (sample data plus anything created via POST)."""
    return students
