#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ckeditor_uploader.fields import RichTextUploadingField 
from django.db import models
import uuid

from photos.models import Photo
from incidents.settings import INCIDENT_CATEGORY, MISCELLANEOUS, PENDING, TRACKING_STATUS
from config.settings.base import AUTH_USER_MODEL

class Incident(models.Model):
    """
    Model of the "contents_incident" table in the database
    """
    category = models.CharField(max_length=30, choices=INCIDENT_CATEGORY, default=MISCELLANEOUS, verbose_name='Type')
    content = RichTextUploadingField(blank=False, verbose_name='Incident')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication le')
    photos = models.ManyToManyField(Photo, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Déclarant', related_name='create_incident')
    zone = models.ForeignKey('condominium.Zone', on_delete=models.CASCADE, related_name='incident_zone')

    def __str__(self):
        return f'Incident - {self.incident_type}'

    def display_author(self):
        """Create a string for the author. This is required to display author in Admin."""
        return self.author.get_full_name()

    display_author.short_description = 'Déclarant'

    class Meta:
        verbose_name_plural = "incidents"

class IncidentDelete(models.Model):
    """
    Intermediate model between "Incident" and "User", defined to add fields
    """
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='deleted_incident')
    deleter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur de la suppression', related_name='incident_deleter')
    deletion_date = models.DateTimeField(auto_now=True, verbose_name='Suppression le')
    deletion_reason = models.CharField(blank=False, max_length=250, verbose_name='Raison de la suppression')

    def display_deleter(self):
        """Create a string for the deleter. This is required to display deleter in Admin."""
        return self.deleter.get_full_name()

    display_deleter.short_description = 'Auteur de la suppression'

class IncidentTracking(models.Model):
    """
    Model of the "contents_incidentTracking" table in the database
    """
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='incident')
    status = models.CharField(max_length=20, choices=TRACKING_STATUS, default=PENDING, verbose_name='Statut')
    status_date = models.DateTimeField(auto_now=True, verbose_name='Date du statut')
    
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name_plural = "Incident status"
