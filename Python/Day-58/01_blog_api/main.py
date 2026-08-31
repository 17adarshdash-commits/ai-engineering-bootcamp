"""
Day 58 Mini Project - Blog API

Routes:
    POST   /users            - create a user
    GET    /users             - list all users
    GET    /users/{id}        - get one user by id

    POST   /posts             - create a post
    GET    /posts              - list all posts
    GET    /posts/{id}         - get one post by id
    PUT    /posts/{id}         - update a post
    DELETE /posts/{id}         - delete a post

    GET    /users/{id}/posts   - list every post belonging to a user

Run:
    uvicorn main:app --reload

Test:
    curl -X POST http://127.0.0.1:8000/users \
        -H "Content-Type: application/json" \
        -d '{"name": "Adarsh", "email": "adarsh@example.com"}'

    curl -X POST http://127.0.0.1:8000/posts \
        -H "Content-Type: application/json" \
        -d '{"title": "First Post", "content": "Hello!", "user_id": 1}'

    curl http://127.0.0.1:8000/users/1/posts

No JWT, auth, comments, likes, pagination, or Docker today - those are
introduced separately. This project is scoped to CRUD + the one-to-many
relationship.
"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, engine, get_db

# Create the users/posts tables on startup if they don't already exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Day 58 - Blog API")


# ---- Users ----

@app.post("/users", response_model=schemas.UserOut, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ---- Posts ----

@app.post("/posts", response_model=schemas.PostOut, status_code=201)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # A post must belong to an existing user - fail fast with a clear
    # error instead of writing an orphaned foreign key.
    user = db.get(models.User, post.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.get("/posts", response_model=list[schemas.PostOut])
def list_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@app.get("/posts/{post_id}", response_model=schemas.PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(models.Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.put("/posts/{post_id}", response_model=schemas.PostOut)
def update_post(post_id: int, updated: schemas.PostUpdate, db: Session = Depends(get_db)):
    post = db.get(models.Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post.title = updated.title
    post.content = updated.content
    db.commit()
    db.refresh(post)
    return post


@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(models.Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()


# ---- Relationship ----

@app.get("/users/{user_id}/posts", response_model=list[schemas.PostOut])
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Walk the relationship instead of writing a manual filter query.
    return user.posts
