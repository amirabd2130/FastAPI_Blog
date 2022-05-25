from ..modules.blogs.models import *
from ..modules.users.models import *


# class Blog(Base):
#     __tablename__ = "blogs"

#     id = Column(String(36), primary_key=True, index=True, nullable=False)
#     date_created = Column(DateTime, nullable=False)
#     date_modified = Column(DateTime, nullable=False)
#     created_by_id = Column(String(36), ForeignKey('users.id'), nullable=False)
#     deleted = Column(Boolean, default=0)
#     title = Column(String(255), nullable=False)
#     body = Column(Text)
#     status = Column(String(50))

#     created_by = relationship("User", back_populates="blogs")


# class User(Base):
#     __tablename__ = "users"

#     id = Column(String(36), primary_key=True, index=True, nullable=False)
#     date_created = Column(DateTime, nullable=False)
#     date_modified = Column(DateTime, nullable=False)
#     deleted = Column(Boolean, default=0)
#     first_name = Column(String(50))
#     last_name = Column(String(50))
#     username = Column(String(50), nullable=False)
#     password = Column(String(255), nullable=False)
#     status = Column(String(50))

#     blogs = relationship("Blog", back_populates="created_by")