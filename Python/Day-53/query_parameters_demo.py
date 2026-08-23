"""query_parameters_demo.py - Optional query parameter filtering.

An in-memory list of employees, exposed through a single GET endpoint
that supports independent, combinable filters via query parameters:

    GET /employees                              -> all employees
    GET /employees?department=IT                -> only IT
    GET /employees?min_salary=60000              -> salary >= 60000
    GET /employees?department=IT&min_salary=60000 -> both filters

Run with:
    uvicorn query_parameters_demo:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Query Parameters Demo",
    description="Optional, combinable query-parameter filtering over an in-memory employee list.",
    version="1.0.0",
)


class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float


employees: list[Employee] = [
    Employee(id=1, name="Asha Rao", department="IT", salary=75000),
    Employee(id=2, name="Vikram Shah", department="IT", salary=55000),
    Employee(id=3, name="Priya Nair", department="HR", salary=62000),
    Employee(id=4, name="Karan Mehta", department="Sales", salary=48000),
    Employee(id=5, name="Divya Iyer", department="Sales", salary=71000),
]


@app.get("/employees", response_model=list[Employee])
def list_employees(
    department: Optional[str] = None,
    min_salary: Optional[float] = None,
):
    """List employees, optionally filtered by department and/or minimum salary.

    Both filters are optional and independent - passing neither returns
    every employee, passing both narrows to records matching both.
    """

    results = employees

    if department is not None:
        results = [e for e in results if e.department == department]

    if min_salary is not None:
        results = [e for e in results if e.salary >= min_salary]

    return results
