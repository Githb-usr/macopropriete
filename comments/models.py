#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ckeditor.fields import RichTextField
from django.db import models
import uuid

from comments.settings import ACTIVATED, STATUS
from config.settings.base import AUTH_USER_MODEL
from contentevent.models import Event
from contentnews.models import News
from incidents.models import Incident

class Comment(models.Model):
    """
    Model of the "contents_comment" table in the database
    """
    content = RichTextField(
        blank=False,
        verbose_name='Commentaire',
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default=ACTIVATED,
        verbose_name='Statut',
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Publication le',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        verbose_name='UUID',
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Auteur',
        related_name='create_comments',
    )
    event = models.ForeignKey(
        Event,
        null=True,
        on_delete=models.CASCADE,
        related_name='add_event_comment',
    )
    news = models.ForeignKey(
        News,
        null=True,
        on_delete=models.CASCADE,
        related_name='add_news_comment',
    )
    incident = models.ForeignKey(
        Incident,
        null=True,
        on_delete=models.CASCADE,
        related_name='add_incident_comment',
    )

    def __str__(self):
        return 'Commentaire de {}'.format(self.author)

    def display_author(self):
        """
        Create a string for the author. This is required to display author in Admin.
        """
        return self.author.get_full_name()

    display_author.short_description = 'Auteur'

    class Meta:
        verbose_name_plural = "comments"
        ordering = ['-creation_date']

class CommentDelete(models.Model):
    """
    Intermediate model between "Comment" and "User", defined to add fields
    """
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='deleted_comment',
    )
    deleter = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Auteur de la suppression',
        related_name='comment_deleter',
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
