# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Project
from src.settings.settings import DEBUG
from src.settings.settings import ROOT_DIR
from src.settings.settings import DATABASE


def create_sessionmaker():
    if DEBUG:
        engine = create_engine('sqlite:///{}/db.sqlite3'.format(ROOT_DIR))
    else:
        URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'.format(
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            host=DATABASE['HOST'],
            name=DATABASE['NAME'],
            port=DATABASE['PORT']
        )
        engine = create_engine(URI)
    return sessionmaker(engine)
