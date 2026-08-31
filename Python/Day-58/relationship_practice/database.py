"""
Database setup: engine, session factory, and declarative base.

Same reusable shape as Day 55/56/57's database.py - this piece doesn't
know anything about User or Post specifically.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./relationship_practice.db"

# check_same_thread=False is SQLite-specific: FastAPI/scripts can use a
# different thread per request, but a single SQLite connection is
# normally restricted to the thread that created it.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Dependency-style helper: yields a session and always closes it
    afterwards (even on error). Used directly as a context in main.py
    since this is a plain script, not a FastAPI app.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
