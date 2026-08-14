# Book Management REST API

A simple CRUD REST API for managing a book inventory, built with **FastAPI**
and backed by **SQLite**. Built as the Day 45 project of the AI Engineering
Bootcamp.

## Overview

The API exposes standard REST endpoints to create, read, update, and delete
books. All books are persisted in a local SQLite database (`books.db`) using
parameterized queries throughout to prevent SQL injection. Validation is
enforced both at the Pydantic model level (types, empty strings, numeric
bounds) and at the route level (duplicate IDs, not-found lookups).

## Folder Structure

```
01_book_api/
├── main.py            # FastAPI app & route definitions
├── models.py           # Pydantic request/response models
├── database.py         # SQLite connection + schema setup
├── crud.py              # Database access layer (parameterized SQL)
├── books.db              # SQLite database file (created on first run)
├── requirements.txt      # Python dependencies
└── README.md              # This file
```

## Book Model

| Field    | Type  | Constraints                  |
|----------|-------|-------------------------------|
| id       | int   | unique, required               |
| title    | str   | required, non-empty            |
| author   | str   | required, non-empty            |
| category | str   | optional                       |
| price    | float | required, must be > 0          |
| stock    | int   | required, must be >= 0         |

## Installation

```bash
cd Python/Day-45/01_book_api
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The SQLite database (`books.db`) and its `books` table are created
automatically on startup if they don't already exist.

## API Endpoints

| Method | Endpoint       | Description             | Success | Error cases                          |
|--------|----------------|--------------------------|---------|----------------------------------------|
| GET    | `/books`       | List all books            | 200     | —                                       |
| GET    | `/books/{id}`  | Retrieve one book          | 200     | 404 if not found                        |
| POST   | `/books`       | Create a new book           | 201     | 409 duplicate id, 422 invalid fields    |
| PUT    | `/books/{id}`  | Update an existing book      | 200     | 404 if not found, 422 invalid fields    |
| DELETE | `/books/{id}`  | Delete a book                 | 204     | 404 if not found                        |

### Validation rules

- `title` and `author` cannot be empty (enforced by Pydantic, → `422`).
- `price` must be greater than `0` (→ `422`).
- `stock` must be greater than or equal to `0` (→ `422`).
- Creating a book with an `id` that already exists returns `409 Conflict`.
- Fetching, updating, or deleting a book that doesn't exist returns
  `404 Not Found`.

## Example Requests

### Create a book

```bash
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "Software Engineering",
        "price": 29.99,
        "stock": 10
      }'
```

Response `201 Created`:
```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "category": "Software Engineering",
  "price": 29.99,
  "stock": 10,
  "id": 1
}
```

### List all books

```bash
curl http://127.0.0.1:8000/books
```

### Get a single book

```bash
curl http://127.0.0.1:8000/books/1
```

### Update a book

```bash
curl -X PUT http://127.0.0.1:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "Software Engineering",
        "price": 24.99,
        "stock": 15
      }'
```

### Delete a book

```bash
curl -X DELETE http://127.0.0.1:8000/books/1
```

Response: `204 No Content`
