"""response_model_demo.py - response_model for automatic filtering/validation.

GET /employee/{id} and POST /employee both declare
response_model=Employee, so the JSON sent back is always shaped exactly
like Employee - regardless of what extra fields the underlying stored
object happens to carry (see `_internal_note` below, which never
reaches the client).

Run with:
    uvicorn response_model_demo:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Response Model Demo",
    description="response_model=Employee filters/validates every response's shape.",
    version="1.0.0",
)


class Employee(BaseModel):
    id: int
    name: str
    department: str


class EmployeeCreate(BaseModel):
    """Shape required to create an employee (id is server-assigned)."""

    name: str
    department: str


# Stored records intentionally carry an extra field that isn't part of
# Employee, to demonstrate that response_model strips it from the
# response.
employees: dict[int, dict] = {
    1: {"id": 1, "name": "Asha Rao", "department": "IT", "_internal_note": "top performer"},
    2: {"id": 2, "name": "Priya Nair", "department": "HR", "_internal_note": "on leave"},
}
_next_id = 3


@app.get("/employee/{id}", response_model=Employee)
def get_employee(id: int):
    """Return one employee. response_model=Employee drops _internal_note."""

    if id not in employees:
        raise HTTPException(status_code=404, detail=f"Employee {id} not found")

    return employees[id]


@app.post("/employee", response_model=Employee, status_code=201)
def create_employee(employee: EmployeeCreate):
    """Create an employee from a validated request body, return it filtered
    through response_model=Employee."""

    global _next_id

    new_employee = {
        "id": _next_id,
        "name": employee.name,
        "department": employee.department,
        "_internal_note": "",
    }
    employees[_next_id] = new_employee
    _next_id += 1

    return new_employee
