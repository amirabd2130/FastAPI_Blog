from datetime import datetime
import uuid
from fastapi import Depends
from sqlalchemy.orm import Session
from ...include import database, exceptions, hashing, models, schemas
from ...modules.authentication.authentication import oauth2_scheme
from ..authentication.jwt_auth import JWTAuth


class User():
    @classmethod
    def create_user(cls, request: schemas.User, db: Session):
        user = db.query(models.User).filter(models.User.username == request.username, models.User.deleted == 0)
        if user.first():
            raise exceptions.USER_EXISTS_EXCEPTION
        else:
            newUser = models.User(
                            id = uuid.uuid4(),
                            date_created = datetime.now().isoformat(),
                            date_modified = datetime.now().isoformat(),
                            first_name = request.first_name,
                            last_name = request.last_name,
                            username = request.username,
                            password = hashing.Hashing.Hash(request.password),
                            status = request.status)
            db.add(newUser)
            db.commit()
            db.refresh(newUser)
            return newUser


    @classmethod
    def get_user_by_id(cls, id: str, db: Session):
        user = db.query(models.User).filter(models.User.id==id, models.User.deleted==0).first()
        if not user:
            raise exceptions.NOT_FOUND_EXCEPTION
        else:
            return user


    @classmethod
    def get_user_by_username(cls, username: str, db: Session):
        user = db.query(models.User).filter(models.User.username==username, models.User.deleted==0).first()
        if user:
            return user


    @classmethod
    def get_current_user(cls, token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
        token_data = JWTAuth.verify_token(token)
        user = User.get_user_by_username(token_data.username, db)
        if not user:
            raise exceptions.CREDENTIALS_EXCEPTION
        return user