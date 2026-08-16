# Day 47 — Response Models, Automatic API Documentation & HTTP Status Review

## 1. Response Models

A route can return any Python object, but without a **response model**
FastAPI just serializes whatever you hand it — including fields you never
meant to expose (password hashes, internal IDs, etc.) and with no schema
guarantee for clients.

`response_model=` fixes that:

```python
class Student(BaseModel):
    id: int
    name: str
    course: str

@app.get("/students", response_model=list[Student])
def get_students():
    return db_students  # can be ORM objects, dicts, anything Student-shaped
```

**What it buys you:**

- **Filtering** — if the object returned has extra fields not declared on
  the model, they're silently dropped from the response. A `User` model
  that includes `hashed_password` internally but whose `UserOut` response
  model omits it means the password never leaves the server.
- **Automatic serialization** — datetimes, enums, nested models, etc. are
  converted to JSON-safe types automatically, consistently, every time.
- **Validation of what you send back** — if your handler accidentally
  returns something that doesn't fit the model, FastAPI raises an error
  instead of silently shipping a malformed response.
- **Accurate docs** — `/docs` and `/redoc` show clients exactly what shape
  to expect, generated straight from the model.

**Hiding sensitive fields** in practice: use two models — an input model
with everything needed to create a resource, and a leaner output model:

```python
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    # no password field -> never serialized in the response
```

## 2. Automatic API Documentation

FastAPI generates interactive docs for free from your route signatures and
Pydantic models — no separate doc-writing step.

- **Swagger UI** — `/docs`. Interactive: expand an endpoint, fill in
  parameters/body, hit "Try it out" and see the real request/response.
- **ReDoc** — `/redoc`. A cleaner, read-only reference view — better for
  browsing a large API than trying requests.
- Both are rendered from the same underlying **OpenAPI schema**, which
  FastAPI builds automatically and serves at `/openapi.json`.

What ends up in the docs, straight from code:

- Path, method, and route summary/description (from the docstring).
- Request body shape (from the Pydantic model type hint).
- Response shape (from `response_model=`).
- Possible status codes (from `status_code=` and any `HTTPException`s you
  raise, if annotated via `responses=`).

No YAML/JSON spec to hand-maintain — the schema and the code can't drift
apart because they're the same source.

## 3. HTTP Status Codes (Review)

| Code | Meaning | When to return it |
|------|---------|---------------------|
| 200 OK | Success | Successful GET / PUT with a response body |
| 201 Created | Resource created | Successful POST |
| 204 No Content | Success, no body | Successful DELETE |
| 400 Bad Request | Malformed request | Client sent something structurally wrong |
| 404 Not Found | Resource doesn't exist | GET/PUT/DELETE on an ID that isn't there |
| 422 Unprocessable Entity | Schema validation failed | Automatic — Pydantic field/type validation failed |

## 4. Key Takeaways

- `response_model=` is as much about *hiding* data as it is about shaping
  it — treat it as the contract for what a client is allowed to see.
- `/docs` and `/redoc` aren't separate work — they fall out of the models
  and type hints you already wrote for validation.
- Prefer the most specific status code available, and let FastAPI/Pydantic
  generate `422` automatically rather than hand-rolling validation errors.
