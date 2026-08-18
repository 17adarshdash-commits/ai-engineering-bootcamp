"""
main.py - Notes API.

All in one file today, as intended - no database, notes live in a plain
Python list for the lifetime of the process. Reinforces middleware and
query-parameter filtering without the overhead of a modular/SQLite
project like Day 48's task manager.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

import time

from fastapi import FastAPI, HTTPException, Request, status
from models import Note, NoteCreate

app = FastAPI(
    title="Notes API",
    description="A simple in-memory notes API with category filtering.",
    version="1.0.0",
)

notes: list[Note] = []
next_id = 1


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Time each request and attach the result as an X-Process-Time header."""
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = f"{process_time:.6f}"
    print(f"{request.method} {request.url.path} completed in {process_time:.6f}s")

    return response


@app.get("/notes", response_model=list[Note])
def get_notes(category: str | None = None) -> list[Note]:
    """Return notes, optionally filtered by category (?category=Study)."""
    if category is None:
        return notes
    return [note for note in notes if note.category == category]


@app.post("/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate) -> Note:
    """Create a note and return it with its assigned id."""
    global next_id
    new_note = Note(id=next_id, **note.model_dump())
    notes.append(new_note)
    next_id += 1
    return new_note


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int) -> None:
    """Delete a note by id. 404 if it doesn't exist."""
    for index, note in enumerate(notes):
        if note.id == note_id:
            del notes[index]
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Note with id {note_id} not found",
    )
