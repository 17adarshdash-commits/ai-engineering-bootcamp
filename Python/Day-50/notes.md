# Day 50 — FastAPI Path Operations, Response Handling, Student Records API

## 1. Path Operations

**What is a path operation?** The combination of an HTTP method (`GET`,
`POST`, `PUT`, `DELETE`, ...) and a URL path, wired to a Python function
via a decorator. FastAPI calls it a "path operation" rather than just a
"route" because the method is part of the identity - `GET /students` and
`POST /students` are two different operations on the same path, each
handled by its own function.

**Path operation decorators** - `@app.get`, `@app.post`, `@app.put`,
`@app.delete` (and `@app.patch`, `@app.options`, ...) register a
function against a path for a specific method:

```python
@app.get("/students")
def list_students():
    ...

@app.post("/students")
def create_student(student: StudentCreate):
    ...

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    ...

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    ...
```

**How each decorator maps to an HTTP request:**
- `GET` - read data, no body, safe and idempotent (calling it twice
  changes nothing).
- `POST` - create a new resource; the client sends a body, the server
  assigns identity (like an id).
- `PUT` - replace/update an existing resource at a known path; idempotent
  (sending the same PUT twice yields the same end state).
- `DELETE` - remove a resource at a known path; no body needed, path
  parameter identifies the target.

## 2. Response Handling

**Returning dictionaries** - FastAPI serializes a plain `dict` straight
to JSON. Fine for quick/ad-hoc responses, but skips the validation and
docs generation a Pydantic `response_model` gives.

**Returning lists** - same idea, a `list[Model]` return type documents
an array response in `/docs` and validates each element.

**Returning custom status codes** - the `status_code` parameter on the
decorator sets the *default* success status for that operation, instead
of FastAPI's default `200`:

```python
@app.post("/students", status_code=201)
def create_student(student: StudentCreate) -> Student:
    ...
```

**`JSONResponse`** - for cases where the status code or headers need to
vary *per call* (not fixed at the decorator level), return a
`JSONResponse` directly:

```python
from fastapi.responses import JSONResponse

@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = find(student_id)
    if student is None:
        return JSONResponse(status_code=404, content={"detail": "Not found"})
    return student
```

In practice `HTTPException` is the more idiomatic way to do the "not
found" branch (see below) - `JSONResponse` is for when the *success*
path itself needs a non-default code or custom headers.

## 3. HTTPException Review

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

`HTTPException` immediately stops the handler and returns an error
response shaped as `{"detail": "..."}` with the given status code.
FastAPI catches it at the framework level, so raising it from anywhere
in a route (or a dependency) short-circuits straight to the client -
no need to manually construct and return an error response.

**When to use it:**
- A requested resource doesn't exist (`404`).
- The request is well-formed but semantically invalid for the current
  state (`409 Conflict`, `400 Bad Request`).
- Any expected failure path that isn't a validation error (Pydantic
  already produces `422` automatically for those).

## 4. Best Practices

- **Keep responses consistent.** Same shape for the same kind of
  resource across every endpoint that returns it - a client shouldn't
  have to special-case `GET` vs `POST` responses for the same model.
- **Return proper HTTP status codes.** `201` for created, `204` for
  deleted-with-no-body, `404` for missing, not a blanket `200` for
  everything.
- **Don't expose unnecessary data.** A `response_model` narrows what
  goes out over the wire to exactly the documented shape, even if the
  internal object carries more fields.
- **Keep route handlers concise.** A route parses input, delegates to
  plain functions/lookups, and shapes the response - business logic
  that grows past a few lines belongs outside the handler.

## 5. Key Takeaways

- The decorator's `status_code` sets the *default* success status;
  `HTTPException` and `JSONResponse` are how a route deviates from that
  default for error or special cases.
- `HTTPException` is preferred over manually returning an error
  `JSONResponse` - it's shorter, and FastAPI documents the possible
  error responses in `/docs` when it sees the pattern.
- A `response_model` (or a typed return annotation) does double duty:
  it documents the API and it filters/validates the outgoing shape,
  which is what keeps "don't expose unnecessary data" enforced
  automatically instead of by discipline.
