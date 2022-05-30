from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import config


DATABASE_URL = config.blog_config['db']['driver']+'://'+config.blog_config['db']['username']+':'+config.blog_config['db']['password']+'@'+config.blog_config['db']['host']+'/'+config.blog_config['db']['db']
# DATABASE_URL = 'postgresql://user:password@postgresserver/db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
