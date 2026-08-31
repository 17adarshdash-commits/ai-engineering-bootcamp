"""
Password hashing + JWT helpers, kept separate from main.py so the
"how" of auth (bcrypt, PyJWT) doesn't clutter the route handlers.

Password hashing
-----------------
bcrypt is used directly (rather than passlib's CryptContext) - passlib
is effectively unmaintained and breaks on recent bcrypt releases, and
FastAPI's own docs now point people at using bcrypt/pwdlib directly.
bcrypt hashes are salted automatically and are one-way: there is no
"decrypt", only "does this password produce this hash" (hash vs.
encryption - encryption is reversible with a key, hashing is not).

JWT
---
PyJWT (same library as Day 55's jwt_demo.py) signs a small payload
(the "claims") with a server-side secret key. The token is not
encrypted - anyone can base64-decode the payload and read it - but it
is tamper-evident: changing a single byte invalidates the signature.
That's why nothing sensitive (passwords, hashes) ever goes in the
payload, only an identifier (`sub`) and an expiry (`exp`).
"""

from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

# In a real app this would be a long, random value pulled from an
# environment variable - never hardcoded or committed like this.
SECRET_KEY = "day60-demo-secret-key-not-for-production-use"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# ---- Password hashing ----

def hash_password(plain_password: str) -> str:
    """Hash a plain-text password for storage. Never store the plain value."""
    password_bytes = plain_password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, password_hash: str) -> bool:
    """Check a login attempt's password against the stored hash."""
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), password_hash.encode("utf-8")
    )


# ---- JWT ----

def create_access_token(subject: str) -> str:
    """Build a signed JWT identifying `subject` (here: the user's email)."""
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> str:
    """
    Verify a token's signature and expiry, and return the `sub` claim.

    Raises jwt.PyJWTError (via jwt.decode) if the token is invalid or
    expired - the caller (main.py's dependency) turns that into a 401.
    """
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload["sub"]
