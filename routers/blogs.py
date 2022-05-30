from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..include import schemas, database
from ..modules.blogs.blogs import Blog
from ..modules.users.users import User


router = APIRouter(
    prefix = '/blog',
    tags = ['Blog'],
)


@router.post('/', status_code = status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.get_current_user)):
    return Blog.create_blog(request, db, currentUser)


@router.get('/', status_code = status.HTTP_200_OK, response_model = List[schemas.BlogFullDetail])
def get_list_of_blogs(db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.get_current_user)):
    return Blog.get_list_of_blogs(db, currentUser)


@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.BlogFullDetail)
def get_one_blog(id: str, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.get_current_user)):
    return Blog.get_one_blog(id, db, currentUser)


@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id: str, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.get_current_user)):
    return Blog.delete_blog(id, db, currentUser)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_blog(id: str, request: schemas.Blog, db: Session = Depends(database.get_db), currentUser: schemas.User = Depends(User.get_current_user)):
    return Blog.update_blog(id, request, db, currentUser)