# Day 58 Mini Project — Blog API

A minimal FastAPI + SQLAlchemy + SQLite blog API with a real one-to-many
relationship (one user, many posts), built on top of today's
relationship basics.

## Technologies

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Models

- **User** — `id`, `name`, `email`
- **Post** — `id`, `title`, `content`, `user_id`

## Relationship

**One User → Many Posts**

`Post.user_id` is a foreign key into `users.id`. `User.posts` and
`Post.author` (`relationship()` + `back_populates`) let the link be
navigated as plain attributes instead of manual joins.

## Files

- `database.py` — engine, session factory, `Base`, and the `get_db`
  dependency.
- `models.py` — `User` and `Post` SQLAlchemy models, linked by
  `user_id` + `relationship()`.
- `schemas.py` — `UserCreate`/`UserOut` and
  `PostCreate`/`PostUpdate`/`PostOut` Pydantic schemas.
- `main.py` — the FastAPI app and routes.

## Endpoints

| Method | Path                 | Description                    |
|--------|----------------------|---------------------------------|
| POST   | `/users`             | Create a user                   |
| GET    | `/users`             | List all users                  |
| GET    | `/users/{id}`        | Get one user                    |
| POST   | `/posts`             | Create a post                   |
| GET    | `/posts`             | List all posts                  |
| GET    | `/posts/{id}`        | Get one post                    |
| PUT    | `/posts/{id}`        | Update a post                   |
| DELETE | `/posts/{id}`        | Delete a post                   |
| GET    | `/users/{id}/posts`  | List all posts belonging to a user |

## Run

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

## Try it

```bash
curl -X POST http://127.0.0.1:8000/users \
    -H "Content-Type: application/json" \
    -d '{"name": "Adarsh", "email": "adarsh@example.com"}'

curl -X POST http://127.0.0.1:8000/posts \
    -H "Content-Type: application/json" \
    -d '{"title": "First Post", "content": "Hello, world!", "user_id": 1}'

curl http://127.0.0.1:8000/posts
curl http://127.0.0.1:8000/posts/1
curl -X PUT http://127.0.0.1:8000/posts/1 \
    -H "Content-Type: application/json" \
    -d '{"title": "First Post (edited)", "content": "Hello again!"}'
curl -X DELETE http://127.0.0.1:8000/posts/1

curl http://127.0.0.1:8000/users/1/posts
```

Or open http://127.0.0.1:8000/docs for interactive Swagger UI.

## Not included today

No JWT, authentication, comments, likes, pagination, or Docker — kept
out on purpose to stay scoped to CRUD + the one-to-many relationship.
Those are introduced separately.
