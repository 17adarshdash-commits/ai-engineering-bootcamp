# Todo API

A minimal in-memory Todo API for reinforcing FastAPI basics — no database,
no CRUD layer, no services, just routes and a Pydantic model.

## Structure

```
01_todo_api/
├── main.py     # FastAPI app + routes
├── models.py   # Pydantic schemas (TodoCreate, Todo)
└── README.md
```

## Fields

- `id` — server-assigned integer
- `task` — the todo text
- `completed` — boolean, defaults to `false`

## Run

```bash
uvicorn main:app --reload
```

- Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Method | Path            | Description               |
|--------|-----------------|----------------------------|
| GET    | `/todos`        | List all todos             |
| POST   | `/todos`        | Create a todo              |
| DELETE | `/todos/{id}`   | Delete a todo by id (404 if missing) |

## Example

```bash
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"task": "Buy milk"}'

curl http://127.0.0.1:8000/todos

curl -X DELETE http://127.0.0.1:8000/todos/1
```

Data resets whenever the server restarts — everything lives in a plain
in-memory list.
