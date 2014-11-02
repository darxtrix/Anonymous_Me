from base import *
import os

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'anonymous_me.wsgi_production.application'

# Database settings

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')