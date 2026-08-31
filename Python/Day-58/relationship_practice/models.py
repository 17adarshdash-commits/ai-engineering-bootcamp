"""
SQLAlchemy models for the one-to-many relationship practice.

User 1 ----------< Many Posts

`Post.user_id` is the real database-level link (a foreign key column).
`User.posts` / `Post.author` are the Python-level convenience added by
relationship() + back_populates, so the link can be navigated as plain
attributes instead of manual queries.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)

    # One user -> many posts. back_populates="author" points at the
    # matching relationship() on Post, keeping both sides in sync.
    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    # The actual foreign key: every post row stores the id of the user
    # that owns it.
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Many posts -> one user. back_populates="posts" mirrors User.posts.
    author = relationship("User", back_populates="posts")
