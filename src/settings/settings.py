import os


DEBUG = os.getenv('DEBUG', default=True)


# APP
HOST = os.getenv('HOST', default='0.0.0.0')
PORT = os.getenv('PORT', default=8000)

# DATABASE
DB_HOST = os.getenv('DB_HOST', default='localhost')
DB_PORT = os.getenv('DB_PORT', default=5432)

SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KLMASFUIHNQEGYRN')
