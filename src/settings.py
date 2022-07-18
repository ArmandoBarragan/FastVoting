import os

env = os.environ
HOST = env.get('HOST')
PORT = env.get('PORT')
DEBUG = env.get('DEBUG')

# Secret key
SECRET_KEY = env.get('SECRET_KEY')
