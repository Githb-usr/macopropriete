#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import environ
import os

from config.settings.base import BASE_DIR

env = environ.Env()
# reading .env file
environ.Env.read_env(os.path.join(BASE_DIR, 'config', '.env'))

environment = env("ENV")
if environment == "local":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
elif environment == "travis":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.travis')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_wsgi_application()
