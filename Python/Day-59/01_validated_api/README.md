Project
-------
Validated Blog API

Technologies
------------
FastAPI
Pydantic
SQLAlchemy
SQLite

Features
--------
User CRUD
Post CRUD
Request validation
Error handling
User/Post relationship

## Models

- **User** — `id`, `name`, `email`, `age`
- **Post** — `id`, `title`, `content`, `user_id`

## Relationship

**One User → Many Posts** (same shape as Day 58's `01_blog_api`).

## Validation (new today)

- `name` — required, non-empty string.
- `email` — required, must be a real email shape (`EmailStr`).
- `age` — required integer, `1 <= age <= 150`.
- `title` / `content` — required, non-empty strings.

Sending the wrong type (e.g. `"age": "hello"`) or a value that fails a
constraint returns **422 Unprocessable Entity** with a JSON body
describing exactly which field failed and why — FastAPI/Pydantic
generate this automatically, no code needed on our end.

## Error handling (new today)

- `POST /posts` with a `user_id` that doesn't exist → **404 User not
  found**.
- `GET /users/{id}` / `GET /posts/{id}` for a missing row → **404**.
- All raised with `fastapi.HTTPException(status_code=..., detail=...)`.

## Files

- `database.py` — engine, session factory, `Base`, and the `get_db`
  dependency.
- `models.py` — `User` and `Post` SQLAlchemy models, linked by
  `user_id` + `relationship()`.
- `schemas.py` — `UserCreate`/`UserOut` and
  `PostCreate`/`PostUpdate`/`PostOut` Pydantic schemas, with
  validation constraints.
- `main.py` — the FastAPI app and routes.

## Endpoints

| Method | Path                 | Description                    |
|--------|----------------------|---------------------------------|
| POST   | `/users`             | Create a user (validated)       |
| GET    | `/users`             | List all users                  |
| GET    | `/users/{id}`        | Get one user (404 if missing)   |
| POST   | `/posts`             | Create a post (404 if user missing) |
| GET    | `/posts`             | List all posts                  |
| GET    | `/posts/{id}`        | Get one post (404 if missing)   |
| PUT    | `/posts/{id}`        | Update a post                   |
| DELETE | `/posts/{id}`        | Delete a post                   |
| GET    | `/users/{id}/posts`  | List all posts belonging to a user |

## Run

```bash
pip install fastapi uvicorn sqlalchemy "pydantic[email]"
uvicorn main:app --reload
```

`pydantic[email]` (installs `email-validator`) is required for
`EmailStr` — without it, FastAPI raises an import error on startup.

## Try it

Valid request:

```bash
curl -X POST http://127.0.0.1:8000/users \
    -H "Content-Type: application/json" \
    -d '{"name": "Alice", "email": "alice@example.com", "age": 21}'
```

Invalid request (wrong types → 422):

```bash
curl -X POST http://127.0.0.1:8000/users \
    -H "Content-Type: application/json" \
    -d '{"name": 123, "email": "not-an-email", "age": "hello"}'
```

Post for a user that doesn't exist (→ 404):

```bash
curl -X POST http://127.0.0.1:8000/posts \
    -H "Content-Type: application/json" \
    -d '{"title": "Hi", "content": "Hello!", "user_id": 999}'
```

Get a missing user/post (→ 404):

```bash
curl http://127.0.0.1:8000/users/999
curl http://127.0.0.1:8000/posts/999
```

Or open http://127.0.0.1:8000/docs for interactive Swagger UI — try
the invalid payloads there to see the 422 response body shape.

## Not included today

No JWT, authentication, comments, likes, pagination, or Docker — kept
out on purpose to stay scoped to validation + error handling. Those
are introduced separately.
