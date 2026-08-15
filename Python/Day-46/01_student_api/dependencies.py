"""
dependencies.py - Reusable FastAPI dependencies.

Centralizing these means:
- Every route that touches the database asks for `Depends(get_db)` and gets
  a connection that is guaranteed to be closed afterward, instead of every
  route opening/closing its own.
- The "does this student exist" 404 check is written once
  (`get_existing_student`) and reused by every route that operates on a
  specific student id, instead of being duplicated in each handler.
"""

import sqlite3
from typing import Iterator

from fastapi import Depends, HTTPException, status

import crud
from database import get_connection
from models import Student


def get_db() -> Iterator[sqlite3.Connection]:
    """Yield a SQLite connection for the duration of a request, then close it."""
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()


def get_existing_student(
    student_id: int, conn: sqlite3.Connection = Depends(get_db)
) -> Student:
    """Look up a student by id or raise 404. Depends on get_db, and is
    itself depended on by any route that needs "a student that exists".
    """
    student = crud.get_student(conn, student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} not found",
        )
    return student
