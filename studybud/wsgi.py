# """
# WSGI config for studybud project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

# application = get_wsgi_application()
# app = application  # Required for Vercel
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

app = get_wsgi_application()  # Vercel requires "app", not just "application"
