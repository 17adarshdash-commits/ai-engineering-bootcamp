"""main.py - Router Demo.

Stays minimal on purpose: create the app, include the routers, done.
Neither student_router nor teacher_router logic lives here - main.py
only wires the two resource modules together.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from student_router import router as student_router
from teacher_router import router as teacher_router

app = FastAPI(
    title="Router Demo",
    description="Demonstrates splitting endpoints into APIRouter modules.",
    version="1.0.0",
)

app.include_router(student_router)
app.include_router(teacher_router)
