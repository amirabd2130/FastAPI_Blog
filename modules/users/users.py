from datetime import datetime
import uuid
from fastapi import Depends
from sqlalchemy.orm import Session
from ...include import database, exceptions, hashing, models, schemas
from ...modules.authentication.authentication import oauth2_scheme
from ..authentication.jwt_auth import JWTAuth


class User():
    @classmethod
    def Create_User(cls, request: schemas.User, db: Session):
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
    def Get_User_by_Id(cls, id: str, db: Session):
        user = db.query(models.User).filter(models.User.id==id, models.User.deleted==0).first()
        if not user:
            raise exceptions.NOT_FOUND_EXCEPTION
        else:
            return user


    @classmethod
    def Get_User_by_Username(cls, username: str, db: Session):
        user = db.query(models.User).filter(models.User.username==username, models.User.deleted==0).first()
        if user:
            return user


    @classmethod
    def Get_Current_User(cls, token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
        token_data = JWTAuth.Verify_Token(token)
        user = User.Get_User_by_Username(token_data.username, db)
        if not user:
            raise exceptions.CREDENTIALS_EXCEPTION
        return user