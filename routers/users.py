from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..include import schemas, database
from ..modules.users.users import User


router = APIRouter(
    prefix = '/user',
    tags = ['User'],
)


@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schemas.UserMinDetail)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return User.create_user(request, db)


@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.UserMinDetail)
def get_user_by_id(id: str, db: Session = Depends(database.get_db)):
    return User.get_user_by_id(id, db)