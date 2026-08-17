# Task Manager API

A CRUD REST API for managing tasks, backed by SQLite, with a modular
architecture: routes, validation, and SQL each live in their own module.

## Structure

```
01_task_manager_api/
├── main.py            # FastAPI app + routes (no SQL here)
├── database.py         # SQLite connection + schema (init_db)
├── crud.py             # All SQL - parameterized queries only
├── models.py            # Priority enum (domain type)
├── schemas.py           # Pydantic request/response models + validation
├── tasks.db              # SQLite file (created on first run)
├── requirements.txt
└── README.md
```

## Task Fields

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Client-supplied, must be unique |
| `title` | str | Required, must not be empty |
| `description` | str | Optional, defaults to `""` |
| `priority` | str | One of `Low`, `Medium`, `High` |
| `completed` | bool | Defaults to `False` |

## Install & Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

- Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Method | Path | Description | Status codes |
|--------|------|--------------|----------------|
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks/{id}` | Get one task | 200, 404 |
| POST | `/tasks` | Create a task | 201, 400 (duplicate id), 422 (validation) |
| PUT | `/tasks/{id}` | Replace a task | 200, 404, 422 |
| DELETE | `/tasks/{id}` | Delete a task | 204, 404 |

## Validation

- **Duplicate ids** — `POST /tasks` with an `id` that already exists
  returns `400 Bad Request`.
- **Empty title** — enforced by a Pydantic field validator on
  `TaskCreate`/`TaskUpdate`; a blank/whitespace-only title returns `422`.
- **Priority** — must be one of `Low`, `Medium`, `High` (a `Priority`
  enum); anything else returns `422`.
- **Completed** — optional on create, defaults to `False`.

## Example

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Write notes", "priority": "High"}'

curl http://127.0.0.1:8000/tasks

curl -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Write notes", "priority": "High", "completed": true}'

curl -X DELETE http://127.0.0.1:8000/tasks/1
```
