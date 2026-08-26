# Day 55 Mini Project — Student API

A minimal FastAPI + SQLAlchemy + SQLite CRUD API for students, built on
top of today's SQLAlchemy basics.

## Files

- `database.py` — engine, session factory, `Base`, and the `get_db`
  dependency (reusable across models).
- `models.py` — the `Student` SQLAlchemy model plus `StudentCreate` /
  `StudentOut` Pydantic schemas.
- `main.py` — the FastAPI app and routes.

## Routes

| Method | Path              | Description         |
|--------|-------------------|----------------------|
| GET    | `/students`       | List all students    |
| POST   | `/students`       | Create a student      |
| GET    | `/students/{id}`  | Get one student       |
| DELETE | `/students/{id}`  | Delete a student      |

## Run

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

## Try it

```bash
curl -X POST http://127.0.0.1:8000/students \
    -H "Content-Type: application/json" \
    -d '{"name": "Adarsh", "department": "AI Engineering", "cgpa": 8.7}'

curl http://127.0.0.1:8000/students
curl http://127.0.0.1:8000/students/1
curl -X DELETE http://127.0.0.1:8000/students/1
```

Or open http://127.0.0.1:8000/docs for interactive Swagger UI.

## Not included yet

No JWT/auth integration — routes are open. That's a natural next step
once the database foundation (this project) is solid, tying together
Day 54's auth concepts with today's SQLAlchemy CRUD.
