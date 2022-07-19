import os

# Import settings
from src.settings import container, local

env = os.environ
DEBUG = env.get('DEBUG')

settings = local if not DEBUG else container

# Assign variables
DEBUG = settings.DEBUG
HOST = settings.HOST
PORT = settings.PORT

SECRET_KEY = settings.SECRET_KEY
