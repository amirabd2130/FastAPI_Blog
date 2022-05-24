from datetime import datetime
from pydantic import BaseModel
from typing import Optional


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
    created_by: str
    modified_by: str
    title: str
    body: str
    status: Optional[str] = 'Draft'

    class Config():
        orm_mode = True



class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    status: Optional[str] = 'Active'

    class Config():
        orm_mode = True


class UserMinDetail(BaseModel):
    first_name: str
    last_name: str
    username: str
    status: Optional[str] = 'Active'

    class Config():
        orm_mode = True


class UserFullDetail(BaseModel):
    id: str
    date_created: datetime
    date_modified: datetime
    created_by: str
    modified_by: str
    first_name: str
    last_name: str
    username: str
    status: Optional[str] = 'Active'

    class Config():
        orm_mode = True