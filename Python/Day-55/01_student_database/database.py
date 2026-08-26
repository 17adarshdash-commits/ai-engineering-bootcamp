"""
Database setup: engine, session factory, and declarative base.

This is the piece any FastAPI + SQLAlchemy project reuses as-is across
models - it doesn't know anything about Student specifically.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"

# check_same_thread=False is SQLite-specific: FastAPI can use a
# different thread per request, but a single SQLite connection is
# normally restricted to the thread that created it.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    FastAPI dependency: yields a session for the duration of one
    request, and always closes it afterwards (even on error).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
