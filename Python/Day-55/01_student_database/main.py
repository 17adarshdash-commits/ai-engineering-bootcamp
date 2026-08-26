"""
Day 55 Mini Project - Simple Student API

Routes:
    GET    /students       - list all students
    POST   /students       - create a student
    GET    /students/{id}  - get one student by id
    DELETE /students/{id}  - delete a student by id

Run:
    uvicorn main:app --reload

Test:
    curl -X POST http://127.0.0.1:8000/students \
        -H "Content-Type: application/json" \
        -d '{"name": "Adarsh", "department": "AI Engineering", "cgpa": 8.7}'

    curl http://127.0.0.1:8000/students
    curl http://127.0.0.1:8000/students/1
    curl -X DELETE http://127.0.0.1:8000/students/1

No JWT integration yet - that's a later day once this foundation is
solid.
"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_db

# Create the students table on startup if it doesn't already exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Day 55 - Student API")


@app.get("/students", response_model=list[models.StudentOut])
def list_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@app.post("/students", response_model=models.StudentOut, status_code=201)
def create_student(student: models.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students/{student_id}", response_model=models.StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(models.Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(models.Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
