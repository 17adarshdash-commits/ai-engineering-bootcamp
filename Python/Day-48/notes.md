# Day 48 — FastAPI + SQLite, Error Handling, CRUD API Design

## 1. FastAPI + SQLite

Everything up through Day 47 stored data in a Python list — gone the
moment the process restarts. A real backend talks to a **database**
instead:

- **Persistence** — data survives restarts, crashes, redeploys.
- **Concurrency** — the database, not app-level Python state, arbitrates
  simultaneous reads/writes.
- **Querying** — filtering, sorting, joins are the database's job, not
  something hand-rolled over a list with a loop.
- **Separation of concerns** — the API layer describes *what* clients can
  do; the database layer owns *how* the data is stored.

SQLite is the natural first database to reach for: it's a single file on
disk, ships with Python's standard library (`sqlite3`), needs no server
process, and is more than enough for a small API.

**Connecting FastAPI to SQLite** — a route handler opens a connection,
runs a query, closes the connection:

```python
import sqlite3

def get_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row  # rows behave like dicts
    return conn

@app.get("/students")
def get_students():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return [dict(row) for row in rows]
```

**Parameterized SQL** — values are always passed as query parameters
(`?` placeholders), never string-formatted into the SQL. This is what
prevents SQL injection:

```python
# Right - value is bound safely, whatever it contains
conn.execute("SELECT * FROM students WHERE id = ?", (student_id,))

# Wrong - a crafted student_id can alter the query itself
conn.execute(f"SELECT * FROM students WHERE id = {student_id}")
```

**Keep connections short-lived** — open a connection per request (or per
function call), do the work, close it. Don't hold one open across
requests; SQLite connections are cheap enough that this costs nothing and
avoids stale/leaked handles.

## 2. Error Handling

`HTTPException` is how a route reports a client-facing error instead of
letting an unhandled exception produce an opaque 500:

```python
from fastapi import HTTPException, status

@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = find_student(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student {student_id} not found",
        )
    return student
```

Raising it anywhere inside a route (including deeper helper functions
called from the route) immediately stops execution and returns the given
status code with `{"detail": "..."}` as the JSON body. Key points:

- `status_code` should be the most specific one for what happened —
  `404` for missing, `400` for malformed/invalid input, not a generic
  `500`.
- `detail` should say what's wrong in terms the client can act on, e.g.
  `"Student with id 7 not found"` rather than `"Error"`.
- Validation errors (a field with the wrong type, a missing required
  field) never need a manual `HTTPException` — Pydantic + FastAPI already
  raise `422` automatically before the route body even runs.

## 3. CRUD API Design

The four operations map directly onto HTTP methods and SQL statements:

| Operation | HTTP Method | SQL |
|-----------|-------------|-----|
| Create | POST | `INSERT INTO ...` |
| Read | GET | `SELECT ...` |
| Update | PUT | `UPDATE ... SET ...` |
| Delete | DELETE | `DELETE FROM ...` |

A consistent shape for a resource `items`:

- `GET /items` — list everything
- `GET /items/{id}` — one resource, 404 if missing
- `POST /items` — create, 201 + the created resource
- `PUT /items/{id}` — full update, 404 if missing
- `DELETE /items/{id}` — remove, 404 if missing, 204 on success

## 4. Response Status Codes (Review)

| Code | Meaning | When to return it |
|------|---------|---------------------|
| 200 OK | Success | Successful GET / PUT with a response body |
| 201 Created | Resource created | Successful POST |
| 204 No Content | Success, no body | Successful DELETE |
| 400 Bad Request | Malformed request | Client sent something structurally wrong |
| 404 Not Found | Resource doesn't exist | GET/PUT/DELETE on an ID that isn't there |
| 422 Unprocessable Entity | Schema validation failed | Automatic — Pydantic field/type validation failed |

## 5. Best Practices

- **Separate routes from database logic.** Routes parse the request,
  call a CRUD function, and shape the response — they shouldn't contain
  raw SQL inline. A dedicated `crud.py` (or `database.py`) module owns
  the actual queries, so the two can change independently.
- **Always validate request data** — let Pydantic models do this at the
  boundary rather than checking types by hand inside the route.
- **Use parameterized SQL queries** — no exceptions, even for
  "trusted" internal values.
- **Return meaningful HTTP errors** — specific status code, specific
  `detail` message.
- **Keep database connections short-lived** — open, use, close; don't
  share a connection across requests.

## 6. Key Takeaways

- Moving from an in-memory list to SQLite is a change in *where data
  lives*, not in the API's shape — the routes still speak Pydantic
  models in and out; only the storage layer underneath changes.
- Parameterized queries aren't an optional safety extra — they're the
  only correct way to put a variable into SQL.
- A small but real modular split (`models`/`schemas`/`database`/`crud`/
  `main`) pays for itself immediately once routes stop containing SQL
  directly.
