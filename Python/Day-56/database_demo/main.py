"""
Day 56 Mini Project - Simple User API

Routes:
    POST   /users       - create a user
    GET    /users       - list all users
    GET    /users/{id}  - get one user by id
    DELETE /users/{id}  - delete a user by id

Run:
    uvicorn main:app --reload

Test:
    curl -X POST http://127.0.0.1:8000/users \
        -H "Content-Type: application/json" \
        -d '{"name": "Adarsh", "email": "adarsh@example.com", "age": 24}'

    curl http://127.0.0.1:8000/users
    curl http://127.0.0.1:8000/users/1
    curl -X DELETE http://127.0.0.1:8000/users/1

Unlike Day 51-53's in-memory list, every request here goes through a
real SQLAlchemy session -> SQLite database file (users.db) that
persists across server restarts.
"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_db

# Create the users table on startup if it doesn't already exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Day 56 - User API")


@app.post("/users", response_model=models.UserOut, status_code=201)
def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users", response_model=list[models.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get("/users/{user_id}", response_model=models.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
