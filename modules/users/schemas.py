from datetime import datetime
from pydantic import BaseModel
from typing import Optional


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