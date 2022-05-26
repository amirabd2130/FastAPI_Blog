from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..include import schemas, database
from ..modules.blogs.blogs import Blog
from ..modules.users.users import User


router = APIRouter(
    prefix = "/blog",
    tags = ["Blog"],
#    dependencies=[Depends(get_token_header)],
#    responses={404: {"description": "Not found"}},
)


@router.post('/', status_code = status.HTTP_201_CREATED)
def Create_Blog(request: schemas.Blog, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.Get_Current_User)):
    return Blog.Create_Blog(request, db, currentUser)


@router.get('/', status_code = status.HTTP_200_OK, response_model = List[schemas.BlogFullDetail])
def Get_List_Of_Blogs(db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.Get_Current_User)):
    return Blog.Get_List_Of_Blogs(db, currentUser)


@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.BlogFullDetail)
def Get_One_Blog(id: str, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.Get_Current_User)):
    return Blog.Get_One_Blog(id, db, currentUser)


@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def Delete_Blog(id: str, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.Get_Current_User)):
    return Blog.Delete_Blog(id, db, currentUser)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def Update_Blog(id: str, request: schemas.Blog, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.Get_Current_User)):
    return Blog.Delete_Blog(id, request, db, currentUser)