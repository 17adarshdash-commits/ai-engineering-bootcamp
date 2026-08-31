"""
Day 60 Mini Project - Basic Auth API

A minimal register / login / protected-profile flow:

    POST /register  - hash the password, store the user
    POST /login      - verify the password, return a JWT
    GET  /profile     - only reachable with a valid "Authorization: Bearer <token>" header

No OAuth2 provider, no refresh tokens - just password hashing + a
signed access token, which is the foundation everything else builds on.

Run:
    uvicorn main:app --reload

Test - register:
    curl -X POST http://127.0.0.1:8000/register \
        -H "Content-Type: application/json" \
        -d '{"name": "Alice", "email": "alice@example.com", "password": "secret123"}'

Test - login (copy the access_token from the response):
    curl -X POST http://127.0.0.1:8000/login \
        -H "Content-Type: application/json" \
        -d '{"email": "alice@example.com", "password": "secret123"}'

Test - protected profile:
    curl http://127.0.0.1:8000/profile \
        -H "Authorization: Bearer <access_token>"

Test - profile without a token (-> 401):
    curl http://127.0.0.1:8000/profile
"""

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import models
import schemas
from auth import create_access_token, decode_access_token, hash_password, verify_password
from database import Base, engine, get_db

# Create the users table on startup if it doesn't already exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Day 60 - Basic Auth API")

# tokenUrl just tells FastAPI's docs UI where a token can be obtained -
# this endpoint still reads the raw "Authorization: Bearer <token>"
# header itself, it doesn't enforce OAuth2's form-encoded login.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> models.User:
    """
    Dependency for protected routes: decode + verify the bearer token,
    then load the user it identifies. Any failure (bad signature,
    expired token, deleted user) becomes a 401.
    """
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        email = decode_access_token(token)
    except jwt.PyJWTError:
        raise credentials_error

    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_error

    return user


@app.post("/register", response_model=schemas.UserOut, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing is not None:
        raise HTTPException(status_code=400, detail="Email already registered")

    # The plain password is hashed here and only the hash is ever
    # written to the database - see auth.hash_password.
    db_user = models.User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/login", response_model=schemas.Token)
def login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.email).first()

    # Same error for "no such user" and "wrong password" - a
    # distinguishable message would let an attacker enumerate which
    # emails are registered.
    invalid_credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
    )

    if user is None or not verify_password(credentials.password, user.password_hash):
        raise invalid_credentials

    access_token = create_access_token(subject=user.email)
    return schemas.Token(access_token=access_token)


@app.get("/profile", response_model=schemas.UserOut)
def profile(current_user: models.User = Depends(get_current_user)):
    # get_current_user has already rejected any missing/invalid/expired
    # token by this point - this route only ever runs for a real user.
    return current_user
