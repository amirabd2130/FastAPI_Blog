from datetime import datetime
import uuid
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ...include import hashing, models, schemas


class User():
    def Create_User(request: schemas.User, db: Session):
        user = db.query(models.User).filter(models.User.username == request.username, models.User.deleted == 0)
        if user.first():
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = f'username {repr(request.username)} already exists')
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


    def Get_One_User(id: str, db: Session):
        user = db.query(models.User).filter(models.User.id==id, models.User.deleted==0).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
        else:
            return user