# Day 59 — Validation + Error Handling

## 1. Pydantic

A Python library that describes data shapes as classes and validates
any data assigned to them at runtime. FastAPI uses it to define what a
request body must look like, and what a response looks like, without
writing manual `if`/`isinstance` checks by hand.

## 2. `BaseModel`

The base class every Pydantic schema inherits from. Declaring a field
with a type annotation (`name: str`) tells Pydantic "this field is
required and must be a `str`" - Pydantic coerces/validates incoming
data against that annotation and raises a validation error if it
doesn't fit.

```python
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(..., gt=0, le=150)
```

- Plain type (`name: str`) → required, must match the type.
- `Field(..., gt=0, le=150)` → adds a constraint on top of the type
  (age must be a positive integer, capped at 150). The `...` marks the
  field as still required (no default).
- `field: str | None = None` (not used today, but the general shape)
  → optional, defaults to `None` if omitted.

## 3. Request validation

FastAPI parses the incoming JSON body against the `BaseModel` declared
as a route parameter (`user: schemas.UserCreate`) *before* the
function body runs. If the body doesn't match - missing field, wrong
type, failed constraint - FastAPI never calls the handler; it returns
a 422 response describing what failed. This is why the handler code
can assume `user.age` is always a valid int in range: invalid data
never gets that far.

## 4. Response validation

The `response_model=schemas.UserOut` on a route does the same check in
reverse: whatever the handler returns gets filtered/validated into the
shape of `UserOut` before it's serialized to JSON. This also means
extra fields on the SQLAlchemy object that aren't part of `UserOut`
are silently dropped from the response - the schema is the contract,
not the DB row.

## 5. Why validation belongs at the API boundary

The boundary (the request body, right as it enters the app) is the
cheapest and clearest place to reject bad data: fail fast with a
precise error message before anything touches the database or business
logic. Pushing validation deeper (e.g. checking inside the route
function, or worse, letting bad data reach SQLAlchemy) means every
downstream function has to defend against malformed input, and errors
get harder to trace back to "the client sent something wrong."

## 6. `HTTPException`

```python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="User not found")
```

A FastAPI-recognized exception: raising it anywhere inside a route
short-circuits the handler and sends a JSON error response
(`{"detail": "User not found"}`) with the given status code, instead
of the request crashing with a raw 500.

## 7. Status codes used today

- **200** → Success (default for `GET`).
- **201** → Created (`POST /users`, `POST /posts` - a new row now
  exists).
- **400** → Bad Request (the request is malformed in a way that isn't
  covered by schema validation - not used directly today, but the
  general "client sent something wrong" code).
- **404** → Not Found - the specific resource (`user_id`, `post_id`)
  doesn't exist. Raised manually with `HTTPException` after checking
  `db.get(...)` returned `None`.
- **422** → Validation Error - the request body failed Pydantic
  validation (wrong type, missing required field, failed constraint).
  Raised automatically by FastAPI, no code needed.
- **500** → Server Error - something broke on the server side that
  wasn't anticipated (a bug, a DB connection failure). Not raised
  intentionally; it's what happens if an *unhandled* exception
  escapes a route.

## 8. Mini project: `01_validated_api/`

Same one-to-many `User`/`Post` shape as Day 58's `01_blog_api/`,
upgraded with:

- `schemas.py` - `EmailStr` for email, `Field(min_length=1)` for
  non-empty strings, `Field(gt=0, le=150)` for age.
- `main.py` - `POST /posts` checks `user_id` exists before creating a
  post (404 if not); `GET /users/{id}` and `GET /posts/{id}` 404 on a
  missing row.

Tried both a valid payload and a deliberately invalid one
(`{"name": 123, "email": "not-an-email", "age": "hello"}`) against
`POST /users` and confirmed FastAPI returns 422 with a field-by-field
breakdown of what failed, without any manual validation code.

See [`01_validated_api/README.md`](01_validated_api/README.md) for the
full endpoint list and how to run it.

## 9. LeetCode: 152. Maximum Product Subarray

File: [`DSA/Arrays/LC152_maximum_product_subarray.py`](../../DSA/Arrays/LC152_maximum_product_subarray.py)

Unlike max *sum* subarray (Kadane's), a single negative number can
flip the sign of the running product, so the best product ending at
index `i` isn't just "extend or restart" - a large negative product
can become the best positive product if multiplied by another
negative.

- Track two running values at each index: `current_max` (best product
  of a subarray ending here) and `current_min` (worst/most negative
  product ending here).
- At each new number `n`:
  - If `n` is negative, `current_max` and `current_min` would swap
    roles if multiplied by `n` (max × negative → could become the new
    min, min × negative → could become the new max) - so swap them
    before computing.
  - `current_max = max(n, current_max * n)`
  - `current_min = min(n, current_min * n)`
  - (the `n` alone option handles restarting the subarray at the
    current index, same as Kadane's `max(n, current_max + n)`.)
- Track a running `result = max(result, current_max)` across all `i`,
  since the global best doesn't have to end at the last index.
- O(n) time, O(1) space.
