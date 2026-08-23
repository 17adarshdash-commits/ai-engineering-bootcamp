# Day 53 — Request Bodies, Response Models, Query Parameters, Employee API

## 1. Request Bodies

**What is a request body?** The payload sent along with an HTTP
request - as opposed to data encoded in the URL (path params, query
params). Where a `GET` reads a resource by identifying it in the URL,
`POST` and `PUT` need to *send* structured data (a new employee, an
updated product, ...), and the URL isn't a good place for that: it's
length-limited, awkward to nest fields in, and not meant to carry a
whole object graph.

**Why `POST` and `PUT` use request bodies:** both operations create or
replace a resource, so the client has to hand the server a full
representation of that resource. `POST /employees` needs the new
employee's `name`, `department`, `salary`, ... - none of that belongs
in the path (`/employees` names the *collection*, not one employee) or
as query params (which are for filtering/options, not payloads).

**How FastAPI parses JSON into Pydantic models:** declare a parameter
whose type is a `BaseModel` subclass, and FastAPI reads the raw
request body, parses it as JSON, and validates/coerces it into an
instance of that model - all before your function body runs. If the
JSON doesn't match the schema (missing field, wrong type), the request
never reaches your code: FastAPI returns a `422 Unprocessable Entity`
with details on what failed.

```python
from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    department: str

@app.post("/employees")
def create_employee(employee: Employee):
    # employee is already a validated Employee instance here
    ...
```

## 2. Response Models

**Why use `response_model=Employee`:** it declares the *output* shape
independently of whatever Python object the function actually returns.
Without it, FastAPI serializes whatever you return as-is - return a
dict with an extra internal field (a password hash, a raw DB row) and
it leaks straight into the JSON response. With `response_model`,
FastAPI filters and re-validates the return value against that model
before sending it, so only the declared fields ever leave the API.

```python
@app.get("/employee/{id}", response_model=Employee)
def get_employee(id: int):
    return db[id]   # any extra keys on this object are dropped
```

**Benefits:**
- **Automatic serialization** - the return value (dict, ORM object,
  dataclass, ...) is converted into the model's shape and then to JSON,
  without manual `.dict()` / `jsonable_encoder` calls.
- **Automatic validation** - if the returned data doesn't satisfy the
  model (wrong type, missing required field), FastAPI raises an error
  instead of silently sending malformed JSON.
- **Hides unnecessary fields** - fields not declared on the response
  model are stripped, even if the underlying object has them. This is
  the standard way to keep sensitive/internal fields out of responses.
- **Better Swagger documentation** - `/docs` shows the exact response
  schema (field names, types, example), generated from the model
  instead of guessed from a live example.

## 3. Advanced Query Parameters

**Optional query parameters** are function parameters with a default
value (usually `None`) that aren't part of the path - FastAPI infers
"not a path param, has a default" as "read this from `?key=value`".

```python
from typing import Optional

@app.get("/employees")
def list_employees(department: Optional[str] = None, min_salary: Optional[float] = None):
    ...
```

- `GET /employees` - no filters, `department` and `min_salary` are
  both `None`.
- `GET /employees?department=IT` - only `department` is set.
- `GET /employees?min_salary=50000` - only `min_salary` is set.

**Combining multiple query parameters for filtering:** each declared
optional parameter independently gates part of the result set - inside
the handler, apply each filter only `if` it was actually provided:

```python
results = employees
if department is not None:
    results = [e for e in results if e.department == department]
if min_salary is not None:
    results = [e for e in results if e.salary >= min_salary]
return results
```

Because each filter is applied conditionally and independently, they
compose - `GET /employees?department=IT&min_salary=60000` filters on
both without any extra code.

## 4. Best Practices

- **Validate all incoming data.** Request bodies should always be
  typed as Pydantic models (never raw `dict`), and query/path params
  should have explicit types - let FastAPI/Pydantic reject bad input
  at the boundary instead of trusting it deeper in the code.
- **Return response models instead of raw dictionaries when possible.**
  `response_model=...` gives every endpoint a documented, filtered
  output shape rather than "whatever this function happened to
  return".
- **Use query parameters for filtering.** Filtering/search options
  belong in the query string (`?department=IT`), not the path -
  the path identifies *which resource*, the query string narrows
  *which subset*.
- **Keep endpoints predictable and RESTful.** Collection routes
  (`/employees`) for list/create, item routes (`/employees/{id}`) for
  read/update/delete one resource, and HTTP methods that match intent
  (`GET` = read, `POST` = create, `PUT` = replace, `DELETE` = remove).
