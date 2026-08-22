# Day 52 — FastAPI Routers, API Organization, Inventory API

## 1. API Routers

**What is an `APIRouter`?** A mini `FastAPI` app - it collects path
operations (`@router.get`, `@router.post`, ...) exactly like `@app.get`
does, but doesn't run on its own. It's mounted onto the real `app` with
`app.include_router(...)` at wiring time.

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/students")
def list_students():
    ...
```

**Why routers exist:** a real API has dozens of endpoints across many
resources (students, teachers, courses, ...). Cramming them all into one
`main.py` makes the file grow without bound and mixes unrelated
concerns together. A router lets each resource's endpoints live in their
own module, so `main.py` doesn't have to know *how* `/students` works -
only that it exists.

**Splitting endpoints into modules** means one file per resource
(`student_router.py`, `teacher_router.py`, ...), each importing only
what it needs (its own models/data) and exporting one `router` object.

**Keeping projects maintainable:** as the API grows, new resources mean
new router modules, not a longer `main.py`. Finding "every endpoint for
students" is a matter of opening one file instead of grepping through
everything.

## 2. Including Routers

`app.include_router(student_router)` copies every path operation
registered on `student_router` onto `app`, as if it had been declared
directly with `@app.get(...)`. Multiple routers can be included; each
adds its own set of routes.

```python
from fastapi import FastAPI
from student_router import router as student_router
from teacher_router import router as teacher_router

app = FastAPI()
app.include_router(student_router)
app.include_router(teacher_router)
```

**Benefits:**
- **Cleaner code** - `main.py` only wires things together; it doesn't
  contain route logic itself.
- **Easier maintenance** - changing how students work touches only
  `student_router.py`.
- **Better scalability** - adding a new resource is "add a new router
  module + one `include_router` call", not "edit an ever-growing file".

## 3. Route Prefixes

`APIRouter(prefix="/students")` lets every route on that router be
defined relative to the resource, without repeating `/students` on each
one:

```python
router = APIRouter(prefix="/students")

@router.get("/")        # -> GET /students
def list_students(): ...

@router.get("/{id}")    # -> GET /students/{id}
def get_student(id: int): ...
```

Examples of the resulting paths: `/students`, `/students/1`.

## 4. Tags

`tags=["Students"]` (passed to `APIRouter(...)` or an individual route)
groups those endpoints under a labeled section in Swagger UI (`/docs`),
so `/students` and `/teachers` endpoints render as separate, clearly
labeled blocks instead of one flat list.

```python
router = APIRouter(prefix="/students", tags=["Students"])
```

## 5. Best Practices

- Group related endpoints together - one router per resource.
- Keep `main.py` minimal - it creates the app and includes routers, and
  does little else.
- Organize large APIs into modules as they grow, rather than
  retrofitting structure after `main.py` becomes unmanageable.

## 6. Key Takeaways

- `APIRouter` is to routes what a Pydantic model is to data shape - a
  way to declare a self-contained unit that gets assembled into the
  final app rather than written inline.
- `prefix` and `tags` are about presentation and DRY-ness (not
  repeating the base path), not routing behavior itself - the same
  routes would still work without them, just with longer paths per
  route and no Swagger grouping.
- The router pattern is the natural next step after Day 51's
  `main.py`/`models.py`/`services.py` split: routers are the "HTTP
  surface" layer, now split further by resource instead of living in
  one file.
