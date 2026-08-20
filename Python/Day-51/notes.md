# Day 51 — FastAPI Dependency Injection Review, Project Structure, Course API

## 1. Dependency Injection (Review)

**What is dependency injection?** Instead of a route function building
everything it needs internally, it *declares* what it needs as a
parameter, and FastAPI supplies it by calling a function on the route's
behalf. `Depends(get_current_user)` tells FastAPI: "before running this
route, call `get_current_user()` and hand me the result."

```python
from fastapi import Depends

def get_api_version():
    return "v1"

@app.get("/")
def home(version: str = Depends(get_api_version)):
    return {"version": version}
```

**Why FastAPI uses `Depends()`:**
- **Reusing common logic** - the same dependency (auth check, DB
  session, pagination params) can be declared on any number of routes
  without copy-pasting its body into each one.
- **Cleaner code** - a route's signature documents exactly what it
  needs, and the route body only contains the logic specific to that
  endpoint, not the setup that got it there.
- **Easier testing** - FastAPI's `app.dependency_overrides` lets a
  dependency be swapped for a fake/stub in tests, without touching the
  route itself. That's much harder when a route calls a function
  directly from inside its body.

## 2. Organizing FastAPI Projects

Everything in one `main.py` works for a tiny demo, but stops scaling
once a project grows past a handful of routes. The usual split:

- **`main.py`** - creates the `FastAPI()` app, wires everything
  together (routers, middleware, startup config). Stays thin.
- **`models.py`** - Pydantic models (request/response shapes) and any
  in-memory/ORM data models.
- **`services.py`** - business logic: the actual "how" behind an
  operation (create a course, apply a filter), independent of HTTP.
- **`routers.py`** (or a `routers/` package) - path operations, grouped
  by resource, each calling out to `services.py` rather than containing
  logic itself.

Today's mini project (Course API) is small enough that `main.py` +
`models.py` covers it without a separate `services.py`/`routers.py` -
but the *habit* of keeping routes thin and logic elsewhere still
applies inside `main.py` itself (see `find_course` as a small
service-like helper).

## 3. Best Practices

- **Keep endpoints thin.** A route parses input, delegates to a helper,
  and shapes the response - it shouldn't itself contain the lookup/
  validation logic inline.
- **Put business logic into helper functions.** `find_course(id)` is
  reused by `GET /courses/{id}`, `PUT /courses/{id}`, and
  `DELETE /courses/{id}` instead of being duplicated three times.
- **Reuse dependencies.** One `get_current_user`-style dependency,
  declared once, can be attached to every route that needs it.
- **Return consistent JSON responses.** Same shape, same status-code
  conventions (201 for create, 204 for delete, 404 for missing) across
  every endpoint - not ad-hoc per route.

## 4. Key Takeaways

- `Depends()` is FastAPI's mechanism for pulling shared setup out of
  route bodies and into standalone, reusable, swappable functions.
- Splitting `main.py` / `models.py` / `services.py` / `routers.py` is
  about separating *wiring* (main), *shape* (models), *logic*
  (services), and *HTTP surface* (routers) - even a small project
  benefits from thinking in those categories, even if some files get
  merged for size.
- A thin route + a small reusable helper (like `find_course`) is the
  same "don't repeat yourself" instinct as `Depends()`, just applied to
  ordinary function calls instead of the DI system.
