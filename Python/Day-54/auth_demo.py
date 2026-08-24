"""
Day 54 - Protected Endpoint Demo

Goal: understand the authentication flow with FastAPI's Depends(),
using a hardcoded API key as a stand-in credential.

Routes:
    GET /            - root, just says hello
    GET /public      - open to anyone, no credential needed
    GET /protected   - requires a correct `x-api-key` header

Run:
    uvicorn auth_demo:app --reload

Test:
    # No key -> 401
    curl -i http://127.0.0.1:8000/protected

    # Wrong key -> 401
    curl -i http://127.0.0.1:8000/protected -H "x-api-key: wrong-key"

    # Correct key -> 200
    curl -i http://127.0.0.1:8000/protected -H "x-api-key: sk-demo-12345"
"""

from fastapi import Depends, FastAPI, Header, HTTPException, status

app = FastAPI(title="Day 54 - Auth Demo")

# Hardcoded for today's exercise only - never do this in a real system.
VALID_API_KEY = "sk-demo-12345"


def verify_api_key(x_api_key: str = Header(...)) -> str:
    """
    Dependency that checks the `x-api-key` header against the known
    valid key. Raises 401 if it's missing (handled by FastAPI itself,
    since the header is a required parameter) or wrong (raised here).

    Because this runs via Depends(), it executes before the route
    body - the route only ever runs once the caller is verified.
    """
    if x_api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return x_api_key


@app.get("/")
def root():
    return {"message": "Day 54 - Auth Demo. Try /public or /protected."}


@app.get("/public")
def public_route():
    """Anyone can call this - no dependency, no credential."""
    return {"message": "This is a public endpoint. No API key needed."}


@app.get("/protected")
def protected_route(api_key: str = Depends(verify_api_key)):
    """
    Only reachable if verify_api_key() did not raise - i.e. the
    caller sent the correct `x-api-key` header.
    """
    return {"message": "You have access"}
