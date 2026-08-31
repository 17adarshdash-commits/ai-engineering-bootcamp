Project
-------
Basic Authentication API

Technologies
------------
FastAPI
SQLAlchemy
SQLite
Pydantic
JWT
Password Hashing

Features
--------
User registration
Password hashing (bcrypt)
Login with JWT issuance
Protected profile endpoint (Bearer token)

## Model

- **User** — `id`, `name`, `email`, `password_hash`

Passwords are **hashed with bcrypt before storage** — there is no
`password` column and the plain password is never written to the
database, only held in memory for the instant it's hashed or verified.

## Auth flow

```
REGISTER -> hash password -> store user
LOGIN    -> verify password -> issue JWT
REQUEST  -> Authorization: Bearer <token> -> verify token -> protected route
```

## Files

- `database.py` — engine, session factory, `Base`, and the `get_db`
  dependency.
- `models.py` — the `User` SQLAlchemy model.
- `schemas.py` — `UserCreate`/`UserOut`/`UserLogin`/`Token` Pydantic
  schemas.
- `auth.py` — password hashing (`bcrypt`) and JWT creation/decoding
  (`PyJWT`) helpers.
- `main.py` — the FastAPI app, routes, and the `get_current_user`
  dependency that protects `/profile`.

## Endpoints

| Method | Path        | Description                                   |
|--------|-------------|------------------------------------------------|
| POST   | `/register` | Create a user; password is hashed before storage |
| POST   | `/login`    | Verify email + password, return a JWT           |
| GET    | `/profile`  | Return the current user — requires a valid `Authorization: Bearer <token>` header |

## Run

```bash
pip install fastapi uvicorn sqlalchemy "pydantic[email]" bcrypt pyjwt
uvicorn main:app --reload
```

`pydantic[email]` (installs `email-validator`) is required for
`EmailStr` — without it, FastAPI raises an import error on startup.

## Try it

Register:

```bash
curl -X POST http://127.0.0.1:8000/register \
    -H "Content-Type: application/json" \
    -d '{"name": "Alice", "email": "alice@example.com", "password": "secret123"}'
```

Login (copy `access_token` from the response):

```bash
curl -X POST http://127.0.0.1:8000/login \
    -H "Content-Type: application/json" \
    -d '{"email": "alice@example.com", "password": "secret123"}'
```

Protected profile:

```bash
curl http://127.0.0.1:8000/profile \
    -H "Authorization: Bearer <access_token>"
```

Profile without a token (→ 401):

```bash
curl http://127.0.0.1:8000/profile
```

Or open http://127.0.0.1:8000/docs for interactive Swagger UI — use
the "Authorize" button with the token from `/login` to try `/profile`.

## Not included today

No refresh tokens, no OAuth2 provider, no roles/permissions — kept out
on purpose to stay scoped to the core register/login/protected-route
flow. Those build on top of this foundation later.
