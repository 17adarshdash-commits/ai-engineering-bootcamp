"""
Pydantic models for the Day 54 Simple Auth API.
"""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    """Request body for POST /login."""

    username: str
    password: str


class LoginResponse(BaseModel):
    """Response body for a successful login."""

    message: str


class ProfileResponse(BaseModel):
    """Response body for GET /profile."""

    username: str
    role: str
