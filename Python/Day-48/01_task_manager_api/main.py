"""
main.py - Task Manager REST API.

Routes only: parse the request, call crud.py, shape the response. All SQL
lives in crud.py, all validation lives in schemas.py, the connection
lives in database.py - this file just wires them together.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

import crud
from database import get_connection, init_db
from fastapi import FastAPI, HTTPException, status
from schemas import Task, TaskCreate, TaskUpdate

app = FastAPI(
    title="Task Manager API",
    description="A CRUD REST API for managing tasks, backed by SQLite.",
    version="1.0.0",
)

init_db()


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    """Return every task."""
    conn = get_connection()
    tasks = crud.get_tasks(conn)
    conn.close()
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    """Return one task by id. 404 if it doesn't exist."""
    conn = get_connection()
    task = crud.get_task(conn, task_id)
    conn.close()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found",
        )
    return task


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate) -> Task:
    """Create a task. 400 if the id is already taken."""
    conn = get_connection()
    if crud.task_exists(conn, task.id):
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Task with id {task.id} already exists",
        )
    new_task = crud.create_task(conn, task)
    conn.close()
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate) -> Task:
    """Fully replace an existing task. 404 if it doesn't exist."""
    conn = get_connection()
    updated = crud.update_task(conn, task_id, task)
    conn.close()
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found",
        )
    return updated


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    """Delete a task by id. 404 if it doesn't exist."""
    conn = get_connection()
    deleted = crud.delete_task(conn, task_id)
    conn.close()
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found",
        )
