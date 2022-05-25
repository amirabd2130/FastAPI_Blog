from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..include import schemas, database
from ..modules.users import users


router = APIRouter(
    prefix = "/user",
    tags = ["User"],
#    dependencies=[Depends(get_token_header)],
#    responses={404: {"description": "Not found"}},
)


@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schemas.UserMinDetail)
def Create_User(request: schemas.User, db: Session = Depends(database.get_db)):
    return users.User.Create_User(request, db)


@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.UserMinDetail)
def Get_One_User(id: str, db: Session = Depends(database.get_db)):
    return users.User.Get_One_User(id, db)