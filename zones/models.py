#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import uuid

class Zone(models.Model):
    """
    Model of the "zones_zone" table in the database
    """
    code = models.CharField(
        max_length=10,
        verbose_name='Code',
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Nom',
    )
    description = models.TextField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name='Description',
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='zones/',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        verbose_name='UUID',
    )

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        verbose_name_plural = "zones"
