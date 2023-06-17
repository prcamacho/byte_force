"""
WSGI config for byte_force project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

import sys

from django.core.wsgi import get_wsgi_application

from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'byte_force.settings')

path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
    sys.path.append(path_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'byte_force.settings'

application = get_wsgi_application()
