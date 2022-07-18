import environ

# Environment setup
env = environ.Env()
environ.Env.read_env()

HOST = env.str('HOST', default='0.0.0.0')
PORT = env.str('PORT', default='8000')
DEBUG = env.bool('DEBUG', default=False)

# Secret key
SECRET_KEY = env.str('SECRET_KEY', default='SECRET_KJHANFNBJINASOFJIDASIOJDF')