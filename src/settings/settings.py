from pathlib import Path
import os


DEBUG = os.getenv('DEBUG', default=True)


ROOT_DIR = Path(os.getcwd())

HOST = os.getenv('HOST', default='0.0.0.0')
PORT = os.getenv('PORT', default=8000)

DATABASE = {
    'HOST': os.getenv('DB_HOST', default='db'),
    'PORT': os.getenv('DB_PORT', default=5432),
    'PASSWORD': os.getenv('DB_PASSWORD', default='postgres'),
    'USER': os.getenv('DB_USER', default='postgres'),
    'NAME': os.getenv('DB_NAME', default='fast_voting')
}

SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KLMASFUIHNQEGYRN')
