from datetime import datetime
from urllib import response
from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session
from . import schemas, models, database
import uuid


app = FastAPI()


models.Base.metadata.create_all(bind = database.engine)


@app.post('/blog', status_code = status.HTTP_201_CREATED)
def CreateBlog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    newBlog = models.Blog(
                        id = uuid.uuid4(),
                        date_created = datetime.now().isoformat(),
                        date_modified = datetime.now().isoformat(),
                        created_by = '1',
                        modified_by = '1',
                        title = request.title,
                        body = request.body,
                        status = request.status)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


@app.get('/blog', status_code = status.HTTP_200_OK, response_model = List[schemas.BlogDetail])
def GetListBlogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).order_by(models.Blog.date_created.desc()).all()
    return blogs


@app.get('/blog/{id}', status_code = status.HTTP_200_OK, response_model = schemas.BlogDetail)
def GetOneBlog(id: str, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id, models.Blog.deleted==0).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        return blog


@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def DeleteBlog(id: str, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        blog.update({'deleted':1})
        db.commit()


@app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED)
def UpdateBlog(id: str, request: schemas.Blog, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        blog.update({'date_modified':datetime.now().isoformat(),'modified_by':'1', 'title':request.title,'body':request.body,'status':request.status})
        db.commit()
        return request





@app.post('/user', status_code = status.HTTP_201_CREATED, response_model = schemas.UserDetail)
def CreateUser(request: schemas.User, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username, models.User.deleted == 0)
    if user.first():
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = f'username {repr(request.username)} already exists')
    else:
        newUser = models.User(
                        id = uuid.uuid4(),
                        date_created = datetime.now().isoformat(),
                        date_modified = datetime.now().isoformat(),
                        created_by = '1',
                        modified_by = '1',
                        first_name = request.first_name,
                        last_name = request.last_name,
                        username = request.username,
                        password = request.password,
                        status = request.status)
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        return newUser


@app.get('/user/{id}', status_code = status.HTTP_200_OK, response_model = schemas.UserDetail)
def GetOneUser(id: str, response: Response, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id==id, models.User.deleted==0).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        return user