from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..include import schemas, database
from ..modules.blogs import blogs


router = APIRouter(
    prefix = "/blog",
    tags = ["Blog"],
#    dependencies=[Depends(get_token_header)],
#    responses={404: {"description": "Not found"}},
)


@router.post('/', status_code = status.HTTP_201_CREATED)
def Create_Blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blogs.Blog.Create_Blog(request, db)


@router.get('/', status_code = status.HTTP_200_OK, response_model = List[schemas.BlogFullDetail])
def Get_List_Of_Blogs(db: Session = Depends(database.get_db)):
    return blogs.Blog.Get_List_Of_Blogs(db)


@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.BlogFullDetail)
def Get_One_Blog(id: str, db: Session = Depends(database.get_db)):
    return blogs.Blog.Get_One_Blog(id, db)


@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def Delete_Blog(id: str, db: Session = Depends(database.get_db)):
    return blogs.Blog.Delete_Blog(id, db)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def Update_Blog(id: str, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blogs.Blog.Delete_Blog(id, request, db)