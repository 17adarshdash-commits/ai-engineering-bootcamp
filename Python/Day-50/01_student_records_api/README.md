# Student Records API

A simple in-memory REST API for managing student records - full CRUD
(`GET`, `POST`, `PUT`, `DELETE`). No database - students live in a
Python list for the lifetime of the process.

## Structure

```
01_student_records_api/
├── main.py       # FastAPI app + routes (single file)
├── models.py     # Pydantic request/response models
└── README.md
```

## Student Fields

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Server-assigned, auto-incrementing |
| `name` | str | Required, must not be empty |
| `department` | str | Required, must not be empty |
| `cgpa` | float | Required, must be between 0.0 and 10.0 |

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
| GET | `/students` | List all students | 200 |
| GET | `/students/{id}` | Get one student | 200, 404 |
| POST | `/students` | Create a student | 201, 422 (validation) |
| PUT | `/students/{id}` | Replace a student's fields | 200, 404, 422 |
| DELETE | `/students/{id}` | Delete a student | 204, 404 |

## Example

```bash
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Cara Lin", "department": "Physics", "cgpa": 9.1}'

curl http://127.0.0.1:8000/students

curl http://127.0.0.1:8000/students/1

curl -X PUT http://127.0.0.1:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Ava Chen", "department": "Computer Science", "cgpa": 9.0}'

curl -X DELETE http://127.0.0.1:8000/students/1
```
