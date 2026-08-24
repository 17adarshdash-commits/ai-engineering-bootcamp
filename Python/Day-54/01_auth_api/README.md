# Simple Auth API

A small FastAPI app demonstrating the basic authentication flow:
hardcoded login credentials plus an API-key-protected route via
`Depends()`.

## Endpoints

| Method | Path       | Auth required | Description                          |
|--------|------------|----------------|---------------------------------------|
| POST   | `/login`   | none           | Validate hardcoded username/password |
| GET    | `/public`  | none           | Open to anyone                        |
| GET    | `/profile` | API key        | Returns username + role               |

## Run

```bash
cd Python/Day-54/01_auth_api
uvicorn main:app --reload
```

## Try it

```bash
# Login - correct credentials -> 200
curl -i -X POST http://127.0.0.1:8000/login \
    -H "Content-Type: application/json" \
    -d '{"username": "admin", "password": "password123"}'

# Login - wrong credentials -> 401
curl -i -X POST http://127.0.0.1:8000/login \
    -H "Content-Type: application/json" \
    -d '{"username": "admin", "password": "wrong"}'

# Public - always 200, no header needed
curl -i http://127.0.0.1:8000/public

# Profile - no key -> 401
curl -i http://127.0.0.1:8000/profile

# Profile - wrong key -> 401
curl -i http://127.0.0.1:8000/profile -H "x-api-key: wrong-key"

# Profile - correct key -> 200
curl -i http://127.0.0.1:8000/profile -H "x-api-key: sk-demo-12345"
```

## Notes

- Credentials and the API key are hardcoded on purpose - this is a
  learning exercise about the authentication *flow*
  (`Depends()` + `HTTPException`), not production security.
- `/login` only checks credentials and returns a success message; it
  does not issue a session or token. That's the natural next step
  once JWTs are introduced later in the course.
- `/profile` is protected the same way as `/protected` in
  `../auth_demo.py` - the `verify_api_key` dependency runs before the
  route body and raises `401` if the `x-api-key` header doesn't match.
