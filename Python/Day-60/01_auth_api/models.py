"""
SQLAlchemy model(s) - the database-facing shape.

Note there is no `password` column anywhere here, only
`password_hash`. The plain password never touches the database - it's
hashed in auth.py before a User row is ever created, and the raw value
is discarded the moment the request finishes.
"""

from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
