import os

env = os.environ

DEBUG = env.get('DEBUG')
HOST = env.get('HOST')
PORT = env.get('PORT')
SECRET_KEY = env.get('SECRET_KEY')
