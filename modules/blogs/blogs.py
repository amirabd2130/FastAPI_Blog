from datetime import datetime
import uuid
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ...include import models, schemas


class Blog():
    def Create_Blog(request: schemas.Blog, db: Session):
        newBlog = models.Blog(
                            id = uuid.uuid4(),
                            date_created = datetime.now().isoformat(),
                            date_modified = datetime.now().isoformat(),
                            created_by_id = '1',
                            title = request.title,
                            body = request.body,
                            status = request.status)
        db.add(newBlog)
        db.commit()
        db.refresh(newBlog)
        return newBlog


    def Update_Blog(id: str, request: schemas.Blog, db: Session):
        blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
        if not blog.first():
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
        else:
            blog.update({'date_modified':datetime.now().isoformat(),'modified_by':'1', 'title':request.title,'body':request.body,'status':request.status})
            db.commit()
            return request


    def Get_One_Blog(id: str, db: Session):
        blog = db.query(models.Blog).filter(models.Blog.id==id, models.Blog.deleted==0).first()
        if not blog:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
        else:
            return blog


    def Get_List_Of_Blogs(db: Session):
        blogs = db.query(models.Blog).order_by(models.Blog.date_created.desc()).all()
        return blogs


    def Delete_Blog(id: str, db: Session):
        blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
        if not blog.first():
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
        else:
            blog.update({'deleted':1})
            db.commit()