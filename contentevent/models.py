#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import uuid

from contentevent.settings import ACTIVATED, EVENT_CATEGORY, MISCELLANEOUS, STATUS
from config.settings.base import AUTH_USER_MODEL

class Event(models.Model):
    """
    Model of the "contents_event" table in the database
    """
    category = models.CharField(
        max_length=30,
        choices=EVENT_CATEGORY,
        default=MISCELLANEOUS,
        verbose_name='Catégorie',
    )
    title = models.CharField(
        blank=False,
        max_length=100,
        verbose_name='Titre',
    )
    content = RichTextUploadingField(
        blank=False,
        verbose_name='Evènement',
    )
    start_date = models.DateTimeField(
        verbose_name='Début de l\'évènement',
    )
    end_date = models.DateTimeField(
        verbose_name='Fin de l\'évènement',
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default=ACTIVATED,
        verbose_name='Statut',
    )
    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Dernière modification',
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Publication le',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True, verbose_name='UUID',
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Auteur',
        related_name='create_events',
    )

    def __str__(self):
        return f'Evènement - {self.title}'

    def display_author(self):
        """
        Create a string for the author. This is required to display author in Admin.
        """
        return self.author.get_full_name()

    display_author.short_description = 'Auteur'

    class Meta:
        verbose_name_plural = "events"

class EventUpdate(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='updated_event',
    )
    updater = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Auteur',
        related_name='event_updater',
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Modification le',
    )
    update_reason = models.CharField(
        max_length=250,
        verbose_name='Raison de la modification',
    )

    def display_updater(self):
        """
        Create a string for the updater. This is required to display updater in Admin.
        """
        return self.updater.get_full_name()

    display_updater.short_description = 'Auteur de la modification'

class EventDelete(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='deleted_event',
    )
    deleter = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Auteur de la suppression',
        related_name='event_deleter',
    )
    deletion_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Suppression le',
    )
    deletion_reason = models.CharField(
        blank=False,
        max_length=250,
        verbose_name='Raison de la suppression',
    )

    def display_deleter(self):
        """
        Create a string for the deleter. This is required to display deleter in Admin.
        """
        return self.deleter.get_full_name()

    display_deleter.short_description = 'Auteur de la suppression'
