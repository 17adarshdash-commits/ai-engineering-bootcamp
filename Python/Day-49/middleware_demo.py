"""
middleware_demo.py - HTTP middleware that times every request.

Wraps every request/response with a timer via @app.middleware("http"):
before call_next() is the request phase, after it is the response phase.
The elapsed time is attached as an X-Process-Time response header and
also printed to the terminal, so it's visible both to the client and to
whoever is running the server.

Run with:
    uvicorn middleware_demo:app --reload

Docs:
    http://127.0.0.1:8000/docs
"""

import time

from fastapi import FastAPI, Request

app = FastAPI(
    title="Middleware Demo",
    description="Demonstrates HTTP middleware that measures request processing time.",
    version="1.0.0",
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Time each request and attach the result as a response header."""
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = f"{process_time:.6f}"
    print(f"{request.method} {request.url.path} completed in {process_time:.6f}s")

    return response


@app.get("/")
def read_root() -> dict:
    """Root endpoint."""
    return {"message": "Welcome to the Middleware Demo API"}


@app.get("/about")
def read_about() -> dict:
    """About endpoint."""
    return {
        "app": "Middleware Demo",
        "purpose": "Show how FastAPI middleware measures request timing.",
    }
