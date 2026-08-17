"""crud.py - All SQL for tasks. Routes never touch SQL directly.

Every function takes an already-open sqlite3.Connection (main.py owns
open/close per request) and uses parameterized queries throughout - no
value is ever string-formatted into a query.
"""

import sqlite3

from schemas import Task, TaskCreate, TaskUpdate


def _row_to_task(row: sqlite3.Row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        description=row["description"] or "",
        priority=row["priority"],
        completed=bool(row["completed"]),
    )


def get_tasks(conn: sqlite3.Connection) -> list[Task]:
    rows = conn.execute(
        "SELECT id, title, description, priority, completed FROM tasks"
    ).fetchall()
    return [_row_to_task(row) for row in rows]


def get_task(conn: sqlite3.Connection, task_id: int) -> Task | None:
    row = conn.execute(
        "SELECT id, title, description, priority, completed FROM tasks WHERE id = ?",
        (task_id,),
    ).fetchone()
    return _row_to_task(row) if row else None


def task_exists(conn: sqlite3.Connection, task_id: int) -> bool:
    row = conn.execute("SELECT 1 FROM tasks WHERE id = ?", (task_id,)).fetchone()
    return row is not None


def create_task(conn: sqlite3.Connection, task: TaskCreate) -> Task:
    conn.execute(
        """
        INSERT INTO tasks (id, title, description, priority, completed)
        VALUES (?, ?, ?, ?, ?)
        """,
        (task.id, task.title, task.description, task.priority.value, int(task.completed)),
    )
    conn.commit()
    return Task(
        id=task.id,
        title=task.title,
        description=task.description,
        priority=task.priority,
        completed=task.completed,
    )


def update_task(conn: sqlite3.Connection, task_id: int, task: TaskUpdate) -> Task | None:
    cursor = conn.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, priority = ?, completed = ?
        WHERE id = ?
        """,
        (task.title, task.description, task.priority.value, int(task.completed), task_id),
    )
    conn.commit()
    if cursor.rowcount == 0:
        return None
    return Task(
        id=task_id,
        title=task.title,
        description=task.description,
        priority=task.priority,
        completed=task.completed,
    )


def delete_task(conn: sqlite3.Connection, task_id: int) -> bool:
    cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    return cursor.rowcount > 0
