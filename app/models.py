"""
This File is used to store models for our ORM Models, For Postgres Database
"""
from typing import Hashable
from sqlalchemy import Column, UUID, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Jobs(Base):
    __tablename__ = "jobs"  # create a table name
    id = Column(Integer, primary_key=True, nullable=False)
    job_title = Column(String, nullable=False)
    job_description = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    applied = Column(Boolean, nullable=False, server_default='FALSE')
    location = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")  # Fetches User Data for us
class Post(Base):
    __tablename__ = "posts"  # create a table name
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")  # Fetches User Data for us


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    phone_number = Column(String)

# a user is only allowed to like a post once

