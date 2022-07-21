from sqlalchemy import create_engine
from psycopg2 import connect
from psycopg2 import Error

from src.settings.settings import DEBUG
from src.settings.settings import ROOT_DIR
from src.settings.settings import DATABASE


def create_db_engine():
    if DEBUG:
        engine = create_engine('sqlite:///{}/db.sqlite3'.format(ROOT_DIR))
    else:
        engine = create_engine('postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'.format(
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            host=DATABASE['HOST'],
            name=DATABASE['NAME'],
            port=DATABASE['PORT']
        ))

    return engine


def connect_to_postgres():
    try:
        connection = connect(
            dbname=DATABASE['NAME'],
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            port=DATABASE['PORT']
        )
    except Error:
        print('Could not connect to database')
        raise Error

    cursor = connection.cursor()
    return connection, cursor
