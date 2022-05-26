from datetime import datetime
import uuid
from fastapi import Depends
from sqlalchemy.orm import Session
from ...include import models, schemas, exceptions


class Blog():
    @classmethod
    def Create_Blog(cls, request: schemas.Blog, db: Session, currentUser: schemas.User):
        newBlog = models.Blog(
                            id = uuid.uuid4(),
                            date_created = datetime.now().isoformat(),
                            date_modified = datetime.now().isoformat(),
                            created_by_id = currentUser.id,
                            title = request.title,
                            body = request.body,
                            status = request.status)
        db.add(newBlog)
        db.commit()
        db.refresh(newBlog)
        return newBlog


    @classmethod
    def Update_Blog(cls, id: str, request: schemas.Blog, db: Session, currentUser: schemas.User):
        blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
        if not blog.first():
            raise exceptions.NOT_FOUND_EXCEPTION
        else:
            blog.update({
                    'date_modified': datetime.now().isoformat(),
                    'title': request.title,
                    'body': request.body,
                    'status': request.status})
            db.commit()
            return request


    @classmethod
    def Get_One_Blog(cls, id: str, db: Session, currentUser: schemas.User):
        blog = db.query(models.Blog).filter(models.Blog.id==id, models.Blog.deleted==0).first()
        if not blog:
            raise exceptions.NOT_FOUND_EXCEPTION
        else:
            return blog


    @classmethod
    def Get_List_Of_Blogs(cls, db: Session, currentUser: schemas.User):
        blogs = db.query(models.Blog).order_by(models.Blog.date_created.desc()).all()
        return blogs


    @classmethod
    def Delete_Blog(cls, id: str, db: Session, currentUser: schemas.User):
        blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
        if not blog.first():
            raise exceptions.NOT_FOUND_EXCEPTION
        else:
            blog.update({
                    'date_modified': datetime.now().isoformat(),
                    'deleted': True})
            db.commit()