import environ

# Environment setup
env = environ.Env()
environ.Env.read_env()


DEBUG = env.bool('DEBUG', default=False)

# Secret key
SECRET_KEY = env.str('SECRET_KEY', default='SECRET_KJHANFNBJINASOFJIDASIOJDF')