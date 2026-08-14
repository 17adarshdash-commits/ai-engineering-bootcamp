# Day 45 — Intro to APIs & FastAPI

## 1. What is an API?

An **API (Application Programming Interface)** is a contract that lets one piece of
software talk to another without either side needing to know the other's internal
implementation. In web development this usually means: a **client** sends a
**request** over HTTP to a **server**, and the server sends back a **response**.

- **Client** — the thing that initiates the conversation (browser, mobile app,
  another server, `curl`, Postman, etc.).
- **Server** — the thing that listens for requests and does the work (looks up
  data, runs a computation, writes to a database) and replies.
- **Request** — what the client sends: a URL, an HTTP method, headers, and
  optionally a body (e.g. JSON payload).
- **Response** — what the server sends back: a status code, headers, and
  optionally a body.
- **HTTP (HyperText Transfer Protocol)** — the protocol (set of rules) that
  requests/responses are exchanged with. It's text-based, stateless, and built
  around verbs (GET, POST, PUT, DELETE, ...) and status codes (200, 404, 500, ...).
- **JSON (JavaScript Object Notation)** — the most common format for API request
  and response bodies. Lightweight, human-readable, maps cleanly to Python
  dicts/lists.

**Why APIs exist:** they let systems built in different languages, on different
machines, owned by different teams/companies, interoperate through a shared,
well-defined interface. Instead of every consumer needing direct database access
or shared code, they just need to know the API's contract.

**Real-world examples:**
- **Google Maps API** — apps embed maps, geocode addresses, get directions
  without building their own mapping data/engine.
- **GitHub API** — tools automate repo/issue/PR management (this very tool,
  `gh`, uses it).
- **OpenAI API** — apps send prompts to a hosted LLM and get completions back
  without hosting the model themselves.

## 2. REST APIs

**REST (REpresentational State Transfer)** is an architectural style for
designing APIs around **resources**.

- **Resource** — a "thing" the API exposes, e.g. a book, a student, a user.
  Identified by a URL, e.g. `/books/5`.
- **Endpoint** — a specific URL + HTTP method combination that performs an
  operation on a resource, e.g. `GET /books/5`.
- **Stateless communication** — the server does not remember anything about the
  client between requests. Every request must carry all the information needed
  to process it (e.g. auth token, IDs). This makes REST APIs easy to scale
  horizontally — any server instance can handle any request.

**HTTP Methods (verbs)** map to CRUD operations:

| Method | Meaning              | Example              |
|--------|----------------------|-----------------------|
| GET    | Read / retrieve      | `GET /books`         |
| POST   | Create               | `POST /books`        |
| PUT    | Update (replace)     | `PUT /books/5`       |
| DELETE | Delete               | `DELETE /books/5`    |

## 3. FastAPI

**FastAPI** is a modern Python web framework for building APIs quickly.

**Why it's popular:**
- Very fast (built on Starlette + Uvicorn, an ASGI server).
- Type hints drive automatic request validation and serialization.
- Automatic interactive documentation (Swagger UI / ReDoc) for free.
- Async support out of the box.
- Great developer experience — minimal boilerplate.

**Installing:**
```bash
pip install fastapi uvicorn
```

**Running a server** (assuming `app` is defined in `first_fastapi_app.py`):
```bash
uvicorn first_fastapi_app:app --reload
```
`--reload` restarts the server automatically when code changes — useful in dev,
never use it in production.

## 4. Path Parameters & Query Parameters

- **Path parameter** — part of the URL path itself, used to identify a specific
  resource. Example: `/books/5` → `5` is the path parameter (book id).
- **Query parameter** — key/value pairs appended to the URL after `?`, used for
  filtering, searching, pagination, optional inputs. Example:
  `/books?author=Alice` → `author=Alice` is a query parameter.

Rule of thumb: path parameters identify *which* resource; query parameters
modify *how* you fetch/filter it.

## 5. Pydantic Models

**Pydantic** `BaseModel` classes describe the *shape* of data (request bodies,
response bodies) using plain Python type hints.

- **Request body validation** — FastAPI parses incoming JSON into the model and
  rejects the request (422 Unprocessable Entity) if it doesn't match.
- **Automatic type checking** — fields are coerced/validated against their
  declared types (`int`, `str`, `float`, etc.).
- **Automatic documentation** — the model's schema is used to generate the
  OpenAPI spec, which powers Swagger UI / ReDoc.

## 6. Automatic API Documentation

FastAPI generates interactive docs automatically from your route definitions
and Pydantic models — no extra work required.

- **Swagger UI** — `http://127.0.0.1:8000/docs` — try requests directly from
  the browser.
- **ReDoc** — `http://127.0.0.1:8000/redoc` — clean, read-only reference docs.

## 7. Best Practices

- **Validate input** — rely on Pydantic models + explicit checks (e.g. price > 0)
  rather than trusting client data.
- **Use proper HTTP methods** — GET for reads (no side effects), POST to
  create, PUT to update, DELETE to remove.
- **Return meaningful responses** — correct status codes (200, 201, 404, 400,
  409, ...) and useful error messages, not just "it failed".
- **Keep business logic separate from API routes** — routes should stay thin
  and delegate to a separate layer (e.g. `crud.py`) that talks to the database.
  This makes the code testable and easier to reason about.
