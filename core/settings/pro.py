from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = pro_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['minadadras.com', 'www.minadadras.com', server_ip]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASS,
        'HOST': 'localhost',
        'PORT': '',
    }
}