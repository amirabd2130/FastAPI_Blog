from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..include import schemas, database
from ..modules.authentication.authentication import Authentication


router = APIRouter(
    prefix = "/login",
    tags = ["User"],
#    dependencies=[Depends(get_token_header)],
#    responses={404: {"description": "Not found"}},
)


@router.post('/', status_code = status.HTTP_201_CREATED)
def Login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return Authentication.Login(request, db)