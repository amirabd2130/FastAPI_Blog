from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(String(36), primary_key=True, index=True)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)
    created_by = Column(String(36))
    modified_by = Column(String(36))
    deleted = Column(Boolean, default=0)
    title = Column(String(255))
    body = Column(Text)
    status = Column(String(50))


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)
    created_by = Column(String(36))
    modified_by = Column(String(36))
    deleted = Column(Boolean, default=0)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    password = Column(String(255))
    status = Column(String(50))
