"""
WSGI config for djangosite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosite.settings')

application = get_wsgi_application()

# # 
# import os
# import sys

# # Add your project directory to the sys.path
# project_home = '/var/www/your_username_pythonanywhere_com'
# if project_home not in sys.path:
#     sys.path.append(project_home)

# # Set environment variables
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosite.settings')

# # Start Django application
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

