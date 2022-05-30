from sqlalchemy.orm import Session
from ...include import hashing, models, exceptions
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .jwt_auth import JWTAuth


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


class Authentication():
    @classmethod
    def login(cls, request: OAuth2PasswordRequestForm, db: Session):
        user = db.query(models.User).filter(models.User.username==request.username, models.User.deleted==0).first()
        if not user:
            raise exceptions.CREDENTIALS_EXCEPTION
        else:
            if not hashing.Hashing.Verify(request.password, user.password):
                raise exceptions.CREDENTIALS_EXCEPTION
            else:
                    access_token = JWTAuth.create_token(data={'sub': user.username})
                    return {'access_token': access_token, 'token_type': 'bearer'}