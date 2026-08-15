# Student Management REST API V2

A CRUD REST API for managing students, built with **FastAPI**, backed by
**SQLite**, and structured around **dependency injection**. Built as the
Day 46 project of the AI Engineering Bootcamp — a follow-up to Day 42's
Student Database System, now exposed as a proper layered API.

## Overview

The API exposes standard REST endpoints to create, read, update, and delete
students. All students are persisted in a local SQLite database
(`students.db`) using parameterized queries throughout to prevent SQL
injection. Two dependencies (`get_db`, `get_existing_student`) are shared
across every route: one hands each request a connection and guarantees it's
closed afterward, the other centralizes the "does this student exist"
404 check instead of repeating it in every handler.

## Folder Structure

```
01_student_api/
├── main.py            # FastAPI app & route definitions
├── database.py         # SQLite connection + schema setup
├── crud.py               # Database access layer (parameterized SQL)
├── models.py               # Pydantic request/response models
├── schemas.py                # Response-envelope schemas (list wrapper, error body)
├── dependencies.py             # Reusable dependencies (DB connection, 404 lookup)
├── students.db                   # SQLite database file (created on first run)
├── requirements.txt                # Python dependencies
└── README.md                         # This file
```

## Student Model

| Field  | Type  | Constraints                          |
|--------|-------|----------------------------------------|
| id     | int   | assigned automatically (primary key)    |
| name   | str   | required, 1-100 chars                    |
| age    | int   | required, between 16 and 100              |
| course | str   | required, 1-100 chars                      |
| cgpa   | float | required, between 0.0 and 10.0              |

## Installation

```bash
cd Python/Day-46/01_student_api
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The SQLite database (`students.db`) and its `students` table are created
automatically on startup if they don't already exist.

## API Endpoints

| Method | Endpoint          | Description             | Success | Error cases              |
|--------|-------------------|--------------------------|---------|-----------------------------|
| GET    | `/students`       | List all students          | 200     | —                             |
| GET    | `/students/{id}`  | Retrieve one student         | 200     | 404 if not found               |
| POST   | `/students`       | Create a new student           | 201     | 422 invalid fields               |
| PUT    | `/students/{id}`  | Update an existing student       | 200     | 404 if not found, 422 invalid fields |
| DELETE | `/students/{id}`  | Delete a student                   | 204     | 404 if not found                       |

### Validation rules

- `name` and `course` must be non-empty, max 100 characters (→ `422`).
- `age` must be between 16 and 100 (→ `422`).
- `cgpa` must be between 0.0 and 10.0 (→ `422`).
- Fetching, updating, or deleting a student that doesn't exist returns
  `404 Not Found`.

## Example Requests

### Create a student

```bash
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Aditi Sharma",
        "age": 21,
        "course": "Computer Science",
        "cgpa": 8.7
      }'
```

Response `201 Created`:
```json
{
  "name": "Aditi Sharma",
  "age": 21,
  "course": "Computer Science",
  "cgpa": 8.7,
  "id": 1
}
```

### List all students

```bash
curl http://127.0.0.1:8000/students
```

### Get a single student

```bash
curl http://127.0.0.1:8000/students/1
```

### Update a student

```bash
curl -X PUT http://127.0.0.1:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Aditi Sharma",
        "age": 22,
        "course": "Computer Science",
        "cgpa": 9.1
      }'
```

### Delete a student

```bash
curl -X DELETE http://127.0.0.1:8000/students/1
```

Response: `204 No Content`

## Dependency Injection

- `get_db` — yields a SQLite connection for the request, closing it in a
  `finally` block regardless of whether the handler succeeds or raises.
- `get_existing_student` — depends on `get_db`, looks the student up by the
  `student_id` path parameter, and raises `404` if it's missing. Every route
  that operates on a specific student (`GET`, `PUT`, `DELETE /students/{id}`)
  declares `Depends(get_existing_student)` instead of duplicating the lookup.
