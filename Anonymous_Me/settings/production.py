from base import *
import os

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'Anonymous_Me.wsgi_production.application'