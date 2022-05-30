from fastapi import FastAPI
from .include import models, database
from .routers import authentication, blogs, users

description = '''
A simple blog API, created by using FastAPI

Entities:
* **Blogs**
* **Users**
* **Comments** --*NOT IMPLEMETED YET*--
* **Tags** --*NOT IMPLEMETED YET*--
* **Admin** --*NOT IMPLEMETED YET*--
'''

app = FastAPI(
    title = 'Blog API',
    description = description,
    version = '0.0.1',
    contact = {
        'name': 'Amir Abdollahi',
        'url': 'https://github.com/amirabd2130/FastAPI_Blog',
        'email': 'amirabd2130@yahoo.com',
    },
    license_info = {
        'name': 'GNU GENERAL PUBLIC LICENSE Version 3',
        'url': 'https://www.gnu.org/licenses/gpl-3.0.en.html',
    },
    openapi_tags = [
        {
            'name': 'User',
            'description': 'Operations with users. The **login** is also here',
        },
        {
            'name': 'Blog',
            'description': 'Operations with blogs',
        },
    ]
)
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(authentication.router)

# create tables if they don't exists in the database
models.Base.metadata.create_all(bind = database.engine)