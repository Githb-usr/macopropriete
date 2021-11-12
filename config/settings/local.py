#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1',]

CRISPY_FAIL_SILENTLY = not DEBUG
