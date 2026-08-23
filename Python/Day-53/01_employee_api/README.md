# Employee API

A simple in-memory REST API for managing employees - full CRUD (`GET`,
`POST`, `PUT`, `DELETE`). No database - employees live in a Python
list for the lifetime of the process.

## Structure

```
01_employee_api/
├── main.py       # FastAPI app + all endpoints
├── models.py     # Pydantic request/response models
└── README.md
```

## Employee Fields

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Server-assigned, auto-incrementing |
| `name` | str | Required, must not be empty |
| `department` | str | Required, must not be empty |
| `salary` | float | Required, must be greater than 0 |

## Install & Run

```bash
pip install fastapi "uvicorn[standard]" pydantic
uvicorn main:app --reload
```

- Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Method | Path | Description | Status codes |
|--------|------|--------------|----------------|
| GET | `/employees` | List all employees | 200 |
| GET | `/employees?department=IT` | List employees filtered by department | 200 |
| GET | `/employees/{id}` | Get one employee | 200, 404 |
| POST | `/employees` | Create an employee | 201, 422 (validation) |
| PUT | `/employees/{id}` | Replace an employee's fields | 200, 404, 422 |
| DELETE | `/employees/{id}` | Delete an employee | 204, 404 |

## Example

```bash
curl -X POST http://127.0.0.1:8000/employees \
  -H "Content-Type: application/json" \
  -d '{"name": "Rahul Verma", "department": "IT", "salary": 68000}'

curl http://127.0.0.1:8000/employees

curl "http://127.0.0.1:8000/employees?department=IT"

curl http://127.0.0.1:8000/employees/1

curl -X PUT http://127.0.0.1:8000/employees/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Asha Rao", "department": "IT", "salary": 80000}'

curl -X DELETE http://127.0.0.1:8000/employees/1
```
