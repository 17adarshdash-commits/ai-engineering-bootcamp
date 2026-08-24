"""
Day 54 Mini Project - Simple Auth API

Routes:
    POST /login    - validate hardcoded credentials, return a message
    GET  /public   - open to anyone
    GET  /profile  - protected by the x-api-key dependency

Run:
    uvicorn main:app --reload

Test:
    # Login - correct credentials -> 200
    curl -i -X POST http://127.0.0.1:8000/login \
        -H "Content-Type: application/json" \
        -d '{"username": "admin", "password": "password123"}'

    # Login - wrong credentials -> 401
    curl -i -X POST http://127.0.0.1:8000/login \
        -H "Content-Type: application/json" \
        -d '{"username": "admin", "password": "wrong"}'

    # Public - always 200
    curl -i http://127.0.0.1:8000/public

    # Profile - no key -> 401 / wrong key -> 401 / correct key -> 200
    curl -i http://127.0.0.1:8000/profile
    curl -i http://127.0.0.1:8000/profile -H "x-api-key: wrong-key"
    curl -i http://127.0.0.1:8000/profile -H "x-api-key: sk-demo-12345"
"""

from fastapi import Depends, FastAPI, Header, HTTPException, status

from models import LoginRequest, LoginResponse, ProfileResponse

app = FastAPI(title="Day 54 - Simple Auth API")

# Hardcoded for this exercise only - never do this in a real system.
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"
VALID_API_KEY = "sk-demo-12345"


def verify_api_key(x_api_key: str = Header(...)) -> str:
    """
    Dependency that protects routes behind a shared API key. Runs
    before the route body via Depends() and short-circuits with a
    401 if the key is wrong.
    """
    if x_api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return x_api_key


@app.post("/login", response_model=LoginResponse)
def login(credentials: LoginRequest):
    """
    Validate against hardcoded credentials. This only checks
    authentication (are these the right credentials?) - it does not
    issue a token/session, since that's out of scope for today.
    """
    if (
        credentials.username != VALID_USERNAME
        or credentials.password != VALID_PASSWORD
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return LoginResponse(message="Login successful")


@app.get("/public")
def public_route():
    """Anyone can access this - no dependency, no credential."""
    return {"message": "This is a public endpoint. No API key needed."}


@app.get("/profile", response_model=ProfileResponse)
def profile(api_key: str = Depends(verify_api_key)):
    """
    Protected by verify_api_key(). Only reachable with the correct
    x-api-key header.
    """
    return ProfileResponse(username=VALID_USERNAME, role="user")
