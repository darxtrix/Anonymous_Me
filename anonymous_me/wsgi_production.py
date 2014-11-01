import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anonymous_me.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
