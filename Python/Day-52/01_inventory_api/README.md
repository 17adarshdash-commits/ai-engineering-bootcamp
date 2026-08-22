# Inventory API

A simple in-memory REST API for managing products - full CRUD (`GET`,
`POST`, `PUT`, `DELETE`). No database - products live in a Python list
for the lifetime of the process.

## Structure

```
01_inventory_api/
├── main.py             # FastAPI app + router registration
├── models.py           # Pydantic request/response models
├── product_router.py   # Product endpoints (APIRouter)
└── README.md
```

## Product Fields

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Server-assigned, auto-incrementing |
| `name` | str | Required, must not be empty |
| `price` | float | Required, must be greater than 0 |
| `quantity` | int | Required, must not be negative |

## Install & Run

```bash
pip install fastapi "uvicorn[standard]" pydantic
uvicorn main:app --reload
```

- Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Method | Path | Description | Status codes |
|--------|------|--------------|----------------|
| GET | `/products` | List all products | 200 |
| GET | `/products/{id}` | Get one product | 200, 404 |
| POST | `/products` | Create a product | 201, 422 (validation) |
| PUT | `/products/{id}` | Replace a product's fields | 200, 404, 422 |
| DELETE | `/products/{id}` | Delete a product | 204, 404 |

## Example

```bash
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Monitor", "price": 8999.0, "quantity": 10}'

curl http://127.0.0.1:8000/products

curl http://127.0.0.1:8000/products/1

curl -X PUT http://127.0.0.1:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Keyboard", "price": 1199.0, "quantity": 20}'

curl -X DELETE http://127.0.0.1:8000/products/1
```
