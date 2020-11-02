"""
WSGI config for cagltransport project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
>>>>>>> 6b4de6aef6f281aa932af2f795ad7357155b6999
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cagltransport.settings')

application = get_wsgi_application()
