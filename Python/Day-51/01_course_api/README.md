# Course API

A simple in-memory REST API for managing courses - full CRUD (`GET`,
`POST`, `PUT`, `DELETE`). No database - courses live in a Python list
for the lifetime of the process.

## Structure

```
01_course_api/
├── main.py       # FastAPI app + routes (single file)
├── models.py     # Pydantic request/response models
└── README.md
```

## Course Fields

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Server-assigned, auto-incrementing |
| `name` | str | Required, must not be empty |
| `instructor` | str | Required, must not be empty |
| `credits` | int | Required, must be between 1 and 6 |

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
| GET | `/courses` | List all courses (uses `Depends(get_current_user)`) | 200 |
| GET | `/courses/{id}` | Get one course | 200, 404 |
| POST | `/courses` | Create a course | 201, 422 (validation) |
| PUT | `/courses/{id}` | Replace a course's fields | 200, 404, 422 |
| DELETE | `/courses/{id}` | Delete a course | 204, 404 |

## Dependency Injection

`GET /courses` declares `user: dict = Depends(get_current_user)` -
FastAPI calls `get_current_user()` and injects the result before the
route runs, the same reusable pattern shown in `dependencies_demo.py`.

## Example

```bash
curl -X POST http://127.0.0.1:8000/courses \
  -H "Content-Type: application/json" \
  -d '{"name": "Compilers", "instructor": "Dr. Nair", "credits": 4}'

curl http://127.0.0.1:8000/courses

curl http://127.0.0.1:8000/courses/1

curl -X PUT http://127.0.0.1:8000/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Data Structures", "instructor": "Dr. Rao", "credits": 3}'

curl -X DELETE http://127.0.0.1:8000/courses/1
```
