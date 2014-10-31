import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Anonymous_Me.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
