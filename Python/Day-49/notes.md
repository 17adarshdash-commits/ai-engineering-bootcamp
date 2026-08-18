# Day 49 — FastAPI Middleware, Query Filtering, Notes API

## 1. FastAPI Middleware

**What is middleware?** A function that sits between the client and the
route handler, wrapping *every* request/response that passes through the
app. Unlike a route (which only runs for its own path), middleware runs
for all of them - it's a single interception point rather than logic
repeated in each handler.

**Why middleware exists** - some concerns are cross-cutting: they apply
to every request regardless of which route handles it. Logging, timing,
auth checks, and CORS headers all fall into this category. Writing that
logic once in middleware avoids either duplicating it into every route
or forgetting it in a new one.

**Request lifecycle** - a request enters the app, passes through each
registered middleware in order, then reaches the matching route
handler. The route runs, produces a response, and that response travels
back out through the same middleware stack (in reverse) before being
sent to the client. This means middleware can act *before* the route
runs (inspect/modify the request) and *after* it returns (inspect/modify
the response) in the same function, split by a single `await call_next(request)`.

**Response lifecycle** - the part of middleware after `call_next`
returns. This is where a response header gets added, a status code
could be inspected, or the final response gets logged - the body has
already been produced by the route at this point.

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)        # route runs here
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

**Example uses:**
- **Logging requests** - method, path, status code, on every request
  without touching route code.
- **Measuring response time** - wrap `call_next` in a timer, as above;
  useful for spotting slow endpoints.
- **Authentication (high level)** - inspect a header/token before
  `call_next` and short-circuit with a 401 response if it's missing or
  invalid, so no route needs to repeat that check. (A dependency is
  usually the better tool for *per-route* auth; middleware suits a
  blanket check across the whole app.)

## 2. Query Filtering

Query parameters (`?key=value` in the URL) let a client narrow a `GET`
down to a subset of results, without needing a separate endpoint per
filter. FastAPI maps them straight to optional function parameters:

```python
@app.get("/notes")
def get_notes(category: str | None = None):
    if category is None:
        return notes
    return [n for n in notes if n.category == category]
```

`GET /notes` returns everything; `GET /notes?category=Study` returns
only the matching subset. The parameter is optional (`str | None = None`)
so the same route serves both cases - no filter means no narrowing.

**Benefits:**
- **Cleaner APIs** - one endpoint (`/notes`) instead of
  `/notes`, `/notes/study`, `/notes/by-category/...`.
- **Flexible searching** - filters can combine (category, plus a search
  term, plus a completed flag) by adding more optional parameters, with
  no new routes.
- **Better user experience** - clients ask for exactly the slice of data
  they need instead of fetching everything and filtering client-side.

## 3. Best Practices

- **Keep middleware lightweight.** It runs on *every* request, so
  expensive work here (a slow DB call, heavy computation) is a tax paid
  by every endpoint, including ones that don't need it.
- **Use query parameters for filtering.** Optional, named, and
  self-documenting in `/docs` - better than encoding filter state into
  the path or requiring a POST body for a read.
- **Return meaningful HTTP errors.** Same principle as prior days -
  specific status code, specific `detail`, not a bare 500.
- **Keep route functions simple.** A route parses input, calls out to
  the actual logic (filtering, CRUD), and shapes the response - it
  shouldn't itself grow into a place where business logic accumulates.

## 4. Key Takeaways

- Middleware and dependencies both run "around" a route, but at
  different scopes: middleware wraps the *entire app*, a dependency is
  opted into per-route. Cross-cutting concerns (timing, logging) belong
  in middleware; per-route concerns (validating one endpoint's specific
  auth requirement) belong in a dependency.
- `call_next` is the hinge of any middleware function - everything
  before it is the request phase, everything after is the response
  phase, and skipping the call entirely means the route never runs.
- Query parameters are the natural fit for optional, read-side filtering
  - they keep `GET` requests idempotent and cacheable, unlike shoving
  filter criteria into a request body.
