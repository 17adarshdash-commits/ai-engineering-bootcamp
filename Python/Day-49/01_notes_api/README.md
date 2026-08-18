# Notes API

A simple in-memory REST API for managing notes, with category filtering
via query parameters and a timing middleware. No database - notes live
in a Python list for the lifetime of the process.

## Structure

```
01_notes_api/
├── main.py       # FastAPI app + routes + middleware (single file)
├── models.py     # Pydantic request/response models
└── README.md
```

## Note Fields

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Server-assigned, auto-incrementing |
| `title` | str | Required, must not be empty |
| `content` | str | Required, must not be empty |
| `category` | str | Required, must not be empty |

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
| GET | `/notes` | List all notes | 200 |
| GET | `/notes?category=Study` | List notes filtered by category | 200 |
| POST | `/notes` | Create a note | 201, 422 (validation) |
| DELETE | `/notes/{id}` | Delete a note | 204, 404 |

## Middleware

Every response includes an `X-Process-Time` header (seconds, as a
float) reporting how long the request took to process. The same value
is printed to the terminal for each request.

## Example

```bash
curl -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "Read Chapter 4", "content": "Focus on DP transitions", "category": "Study"}'

curl http://127.0.0.1:8000/notes

curl "http://127.0.0.1:8000/notes?category=Study"

curl -X DELETE http://127.0.0.1:8000/notes/1
```
