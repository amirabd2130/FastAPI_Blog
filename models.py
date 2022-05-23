from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from .database import Base


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    date_entered = Column(DateTime)
    deleted= Column(Boolean, default=0)
    title = Column(String(255))
    body = Column(Text)
    status = Column(String(50), default='Published')
