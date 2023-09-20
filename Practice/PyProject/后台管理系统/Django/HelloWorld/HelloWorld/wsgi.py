# /wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目

"""
WSGI config for HelloWorld project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HelloWorld.settings")

application = get_wsgi_application()
