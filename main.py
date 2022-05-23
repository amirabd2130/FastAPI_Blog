from datetime import datetime
from fastapi import FastAPI
from typing import Optional
from . import schemas, models, database


app = FastAPI()


models.Base.metadata.create_all(bind=database.engine)


@app.get('/blog')
def blog(limit:Optional[int]=None, published:Optional[bool]=None):
    return {'data':{'limit':limit, 'published':published}}

   
@app.get('/blog/{id}')
def blog(id:int):
    return {'data':{'id':id}}


@app.post('/blog')
def CreateBlog(request: schemas.Blog):
    return {'data': {
                    'id': '123-456-789',
                    'title': request.title,
                    'date_entered': datetime.now().isoformat()}}