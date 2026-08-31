"""
SQLAlchemy models - the database-facing shape.

User 1 ----------< Many Posts

Pydantic request/response schemas live in schemas.py, kept separate so
the API contract doesn't have to leak every internal DB detail.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)

    # One user -> many posts.
    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Many posts -> one user.
    author = relationship("User", back_populates="posts")
