from datetime import datetime
from urllib import response
from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session
from . import hashing, schemas, models, database
import uuid


description = """
A simple blog API using FastAPI

Entities:
* **Blogs**
* **Users**
* **Comments** (--NOT IMPLEMETED YET--)
"""

tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Blog",
        "description": "Manage blogs.",
    },
]
app = FastAPI(
    title="Blog API",
    description=description,
    version="0.0.1",
    contact={
        "name": "Amir Abdollahi",
        "url": "https://github.com/amirabd2130/FastAPI_Blog",
        "email": "amirabd2130@yahoo.com",
    },
    license_info={
        "name": "GNU GENERAL PUBLIC LICENSE Version 3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    openapi_tags=tags_metadata,
)

models.Base.metadata.create_all(bind = database.engine)



@app.post('/blog', status_code = status.HTTP_201_CREATED, tags=['Blog'])
def Create_Blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
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


@app.get('/blog', status_code = status.HTTP_200_OK, response_model = List[schemas.BlogFullDetail], tags=['Blog'])
def Get_List_Of_Blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).order_by(models.Blog.date_created.desc()).all()
    return blogs


@app.get('/blog/{id}', status_code = status.HTTP_200_OK, response_model = schemas.BlogFullDetail, tags=['Blog'])
def Get_One_Blog(id: str, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id, models.Blog.deleted==0).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        return blog


@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT, tags=['Blog'])
def Delete_Blog(id: str, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        blog.update({'deleted':1})
        db.commit()


@app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED, tags=['Blog'])
def Update_Blog(id: str, request: schemas.Blog, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.deleted == 0)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        blog.update({'date_modified':datetime.now().isoformat(),'modified_by':'1', 'title':request.title,'body':request.body,'status':request.status})
        db.commit()
        return request





@app.post('/user', status_code = status.HTTP_201_CREATED, response_model = schemas.UserMinDetail, tags=['User'])
def Create_User(request: schemas.User, db: Session = Depends(database.get_db)):
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
                        password = hashing.Hashing.Hash(request.password),
                        status = request.status)
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        return newUser


@app.get('/user/{id}', status_code = status.HTTP_200_OK, response_model = schemas.UserMinDetail, tags=['User'])
def Get_One_User(id: str, response: Response, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id==id, models.User.deleted==0).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'record with id {repr(id)} deos not exist or has been deleted')
    else:
        return user