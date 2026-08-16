"""
main.py - Todo API.

In-memory only - no database, no CRUD layer, no services. Just enough
structure to reinforce FastAPI basics: routes, Pydantic models, and
response_model=.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from fastapi import FastAPI, HTTPException, status

from models import Todo, TodoCreate

app = FastAPI(
    title="Todo API",
    description="A minimal in-memory todo list API.",
    version="1.0.0",
)

todos: list[Todo] = []
next_id = 1


@app.get("/todos", response_model=list[Todo])
def get_todos() -> list[Todo]:
    """Return every todo."""
    return todos


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate) -> Todo:
    """Create a new todo and return it, with a server-assigned id."""
    global next_id
    new_todo = Todo(id=next_id, task=todo.task, completed=todo.completed)
    todos.append(new_todo)
    next_id += 1
    return new_todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int) -> None:
    """Delete a todo by id. 404 if it doesn't exist."""
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with id {todo_id} not found",
    )
