from sqlalchemy import create_engine

from src.settings.settings import DEBUG
from src.settings.settings import ROOT_DIR
from src.settings.settings import DATABASE


def create_db_engine():
    if DEBUG:
        engine = create_engine('sqlite:///{}/db.sqlite3'.format(ROOT_DIR))
    else:
        engine = create_engine('postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            host=DATABASE['HOST'],
            name=DATABASE['NAME']
        ))
    return engine
