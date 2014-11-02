from base import *
import os

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'anonymous_me.wsgi_production.application'

# Database settings

# Parse database configuration from $DATABASE_URL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbpf1qhlrdvrej',
        'HOST': 'ec2-54-83-204-85.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'jpyobasmfwtoys',
        'PASSWORD': '4e_vRRrZ80sLm-1h048SrdzLyM',
    }
}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')