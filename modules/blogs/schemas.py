from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from ...modules.users import schemas


class Blog(BaseModel):
    title: str
    body: str
    status: Optional[str] = 'Draft'


class BlogMinDetail(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True


class BlogFullDetail(BaseModel):
    id: str
    date_created: datetime
    date_modified: datetime
    created_by: schemas.UserMinDetail
    title: str
    body: str
    status: Optional[str] = 'Draft'

    class Config():
        orm_mode = True