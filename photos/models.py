#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import uuid

from config.settings.base import AUTH_USER_MODEL

class Photo(models.Model):
    """
    Model of the "photos_photo" table in the database
    """
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True, verbose_name='Légende')
    uploader = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Uploadé par')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date d\'upload')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')

    def __str__(self):
        return f'{self.caption}'
