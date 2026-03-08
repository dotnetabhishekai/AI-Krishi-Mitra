"""
WSGI config for krishi_mitra project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krishi_mitra.settings')

application = get_wsgi_application()
