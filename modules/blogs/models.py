from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime, Text
from sqlalchemy.orm import relationship
from ...include.database import Base
from ...modules.users.models import *


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(String(36), primary_key=True, index=True, nullable=False)
    date_created = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)
    created_by_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    deleted = Column(Boolean, default=0)
    title = Column(String(255), nullable=False)
    body = Column(Text)
    status = Column(String(50))

    created_by = relationship('User', back_populates='blogs')