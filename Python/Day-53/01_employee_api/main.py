"""main.py - Employee API.

Full CRUD over an in-memory list of employees, plus filtering by
department via a query parameter.

Run with:
    uvicorn main:app --reload

Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from models import Employee, EmployeeCreate, EmployeeUpdate

app = FastAPI(
    title="Employee API",
    description="A simple in-memory REST API for managing employees.",
    version="1.0.0",
)

employees: list[Employee] = [
    Employee(id=1, name="Asha Rao", department="IT", salary=75000),
    Employee(id=2, name="Vikram Shah", department="IT", salary=55000),
    Employee(id=3, name="Priya Nair", department="HR", salary=62000),
]
_next_id = 4


def _find_employee(employee_id: int) -> Employee:
    for employee in employees:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")


@app.get("/employees", response_model=list[Employee])
def list_employees(department: Optional[str] = None):
    """List employees, optionally filtered by department (?department=IT)."""

    if department is None:
        return employees

    return [e for e in employees if e.department == department]


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    """Get a single employee by id."""

    return _find_employee(employee_id)


@app.post("/employees", response_model=Employee, status_code=201)
def create_employee(employee: EmployeeCreate):
    """Create a new employee. id is server-assigned."""

    global _next_id

    new_employee = Employee(id=_next_id, **employee.model_dump())
    employees.append(new_employee)
    _next_id += 1

    return new_employee


@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeUpdate):
    """Replace an existing employee's fields (id stays the same)."""

    existing = _find_employee(employee_id)
    updated = Employee(id=existing.id, **employee.model_dump())

    index = employees.index(existing)
    employees[index] = updated

    return updated


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int):
    """Delete an employee by id."""

    existing = _find_employee(employee_id)
    employees.remove(existing)
