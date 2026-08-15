"""
crud.py - Database access layer for students.

All SQL lives here, kept separate from the API routes in main.py and the
dependency wiring in dependencies.py. Every query is parameterized (using
`?` placeholders) to avoid SQL injection.
"""

import sqlite3
from typing import List, Optional

from models import Student, StudentCreate, StudentUpdate


def _row_to_student(row: sqlite3.Row) -> Student:
    return Student(
        id=row["id"],
        name=row["name"],
        age=row["age"],
        course=row["course"],
        cgpa=row["cgpa"],
    )


def get_all_students(conn: sqlite3.Connection) -> List[Student]:
    rows = conn.execute("SELECT * FROM students ORDER BY id").fetchall()
    return [_row_to_student(row) for row in rows]


def get_student(conn: sqlite3.Connection, student_id: int) -> Optional[Student]:
    row = conn.execute(
        "SELECT * FROM students WHERE id = ?", (student_id,)
    ).fetchone()
    return _row_to_student(row) if row else None


def create_student(conn: sqlite3.Connection, student: StudentCreate) -> Student:
    cursor = conn.execute(
        "INSERT INTO students (name, age, course, cgpa) VALUES (?, ?, ?, ?)",
        (student.name, student.age, student.course, student.cgpa),
    )
    conn.commit()
    return Student(id=cursor.lastrowid, **student.model_dump())


def update_student(
    conn: sqlite3.Connection, student_id: int, student: StudentUpdate
) -> Optional[Student]:
    cursor = conn.execute(
        """
        UPDATE students
        SET name = ?, age = ?, course = ?, cgpa = ?
        WHERE id = ?
        """,
        (student.name, student.age, student.course, student.cgpa, student_id),
    )
    conn.commit()
    if cursor.rowcount == 0:
        return None
    return Student(id=student_id, **student.model_dump())


def delete_student(conn: sqlite3.Connection, student_id: int) -> bool:
    cursor = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    return cursor.rowcount > 0
