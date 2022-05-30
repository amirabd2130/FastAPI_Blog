from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from ...include.database import Base
from ...modules.blogs.models import *


class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, index=True, nullable=False)
    date_created = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)
    deleted = Column(Boolean, default=0)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    status = Column(String(50))

    blogs = relationship('Blog', back_populates='created_by')