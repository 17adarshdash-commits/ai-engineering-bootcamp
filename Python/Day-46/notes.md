# Day 46 — FastAPI Project Structure, Dependency Injection & Validation

## 1. FastAPI Project Structure

A single `main.py` works fine for a toy app, but real projects split it up so
each file has one job:

| File / folder | Responsibility |
|----------------|-----------------|
| `main.py`      | Create the `FastAPI` app, wire up routers/startup events |
| `routers/`     | Route definitions — thin handlers that call into services |
| `models/`      | Pydantic schemas for request/response validation |
| `services/`    | Business logic — the actual "what does this endpoint do" |
| `database/`    | DB connection setup, schema creation |
| `schemas/`     | (sometimes split from `models/`) DB-row ↔ API-shape mapping |

```
project/
├── main.py
├── routers/
├── models/
├── services/
├── database/
└── schemas/
```

**Why bother?**
- **Separation of concerns** — a route handler shouldn't contain SQL, and SQL
  shouldn't know about HTTP status codes.
- **Testability** — service functions are plain Python, easy to unit test
  without spinning up a server.
- **Scale** — as endpoints multiply, a flat `main.py` becomes unreadable;
  routers let you group by resource (`/students`, `/orders`, ...) and mount
  them independently (`app.include_router(...)`).
- **Reuse** — the same service function can back multiple routes, or be
  reused outside the API entirely (a CLI script, a background job).

## 2. Dependency Injection

**Dependency injection (DI)** means a function declares *what it needs*
rather than constructing it itself — FastAPI supplies it via `Depends`.

```python
from fastapi import Depends

def get_message():
    return "Hello"

@app.get("/")
def home(message: str = Depends(get_message)):
    return {"message": message}
```

FastAPI calls `get_message()` for you and injects the result as `message`.

**Why FastAPI leans on this so heavily:**
- **Reusing common logic** — pagination params, current-user lookup,
  a "does this ID exist" check — write it once, `Depends()` it everywhere.
- **Injecting database connections** — a dependency can `yield` a connection
  and close it afterward, guaranteeing cleanup even on errors:
  ```python
  def get_db():
      conn = get_connection()
      try:
          yield conn
      finally:
          conn.close()
  ```
- **Injecting authentication** — a dependency can read a header/token,
  validate it, and either return the current user or raise `HTTPException`.
  Every route that needs auth just adds `Depends(get_current_user)`.
- **Composability** — dependencies can themselves depend on other
  dependencies, and FastAPI resolves the whole chain automatically.
- **Testability** — `app.dependency_overrides` lets tests swap a real DB
  dependency for a fake one without touching route code.

## 3. Request Validation

Pydantic's `Field()` attaches constraints on top of plain type hints:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
```

- `...` (Ellipsis) as the first positional arg means the field is
  **required** — no default value.
- **String constraints** — `min_length`, `max_length`.
- **Numeric constraints** — `gt` / `ge` (greater than / greater-or-equal),
  `lt` / `le` (less than / less-or-equal).
- **Default values** — `Field(default=0, ge=0)` makes a field optional with
  a fallback.
- **Optional fields** — `Optional[str] = None` (or `str | None = None`)
  marks a field as not required at all.

If the incoming JSON violates any constraint, FastAPI automatically returns
`422 Unprocessable Entity` with a detailed error body — no manual `if`
checks needed for shape/type/range validation.

## 4. HTTP Status Codes

| Code | Meaning | When to return it |
|------|---------|---------------------|
| 200 OK | Success | Successful GET / PUT that returns a body |
| 201 Created | Resource created | Successful POST |
| 204 No Content | Success, no body | Successful DELETE |
| 400 Bad Request | Malformed request | Client sent something structurally wrong (rare once Pydantic validates shape) |
| 404 Not Found | Resource doesn't exist | GET/PUT/DELETE on an ID that isn't there |
| 422 Validation Error | Request failed schema validation | Automatic — Pydantic field constraints failed |
| 500 Internal Server Error | Unexpected server-side failure | Uncaught exception — should be rare and logged |

Rule of thumb: prefer the most specific code available (`404` over a bare
`400`), and let Pydantic/FastAPI generate `422` for you rather than
hand-rolling validation errors.

## 5. Best Practices

- **Keep route handlers small** — a route should parse input, call one
  service/CRUD function, and translate the result into an HTTP response.
- **Move business logic into service functions** — anything beyond
  "look up this ID and format it" belongs outside `main.py`/routers.
- **Validate inputs using Pydantic** — lean on `Field()` constraints instead
  of manual `if` checks wherever possible.
- **Return meaningful status codes** — see the table above.
- **Reuse dependencies** — `Depends()` the same DB/auth/pagination logic
  across every route that needs it instead of duplicating it.
