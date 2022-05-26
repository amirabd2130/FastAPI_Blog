from setuptools import setup

setup(
    name = 'FastAPI_Blog',
    version = '0.0.1',
    license = "GNU GENERAL PUBLIC LICENSE Version 3",
    description = 'A simple blog API using FastAPI',
    author = 'Amir Abdollahi',
    author_email = 'amirabd2130@yahoo.com',
    url = "https://github.com/amirabd2130/FastAPI_Blog",
    packages = ['FastAPI_Blog'],
    install_requires = ['fastapi', 'uvicorn', 'pymysql', 'sqlalchemy', 'python-jose', 'cryptography', 'passlib', 'bcrypt', 'python-multipart'],
)