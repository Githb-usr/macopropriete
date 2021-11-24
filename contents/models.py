#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
import uuid

from contents.choices import ACTIVATED, NEWS_CATEGORY, CONTENT_STATUS, EVENT_CATEGORY, FAQ_CATEGORY, INCIDENT_CATEGORY, MISCELLANEOUS, PENDING, TRACKING_STATUS
from config.settings.base import AUTH_USER_MODEL

class Photo(models.Model):
    """
    Model of the "contents_photo" table in the database
    """
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True, verbose_name='Légende')
    uploader = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Uploadé par')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date d\'upload')

class News(models.Model):
    """
    Model of the "contents_news" table in the database
    """
    category = models.CharField(max_length=30, choices=NEWS_CATEGORY, default=MISCELLANEOUS, verbose_name='Catégorie')
    title = models.CharField(blank=False, max_length=100, verbose_name='Titre')
    content = models.TextField(blank=False, verbose_name='News')
    status = models.CharField(max_length=30, choices=CONTENT_STATUS, default=ACTIVATED, verbose_name='Statut')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication le')
    photos = models.ManyToManyField(Photo, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_news')
    news_update_user = models.ManyToManyField(AUTH_USER_MODEL, through='contents.NewsUpdate', related_name='news_update_user')
    news_delete_user = models.ManyToManyField(AUTH_USER_MODEL, through='contents.NewsDelete', related_name='news_delete_user')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'uuid': self.uuid})

    def display_author(self):
        """Create a string for the author. This is required to display author in Admin."""
        return self.author.get_full_name()

    display_author.short_description = 'Auteur'

    class Meta:
        verbose_name_plural = "news"
        ordering = ['-creation_date']

class NewsUpdate(models.Model):
    """
    Intermediate model between "News" and "User", defined to add fields
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='News modifiée', related_name='updated_news')
    updater = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='news_updater')
    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='Modification le')
    update_reason = models.CharField(max_length=250, verbose_name='Raison de la modification')

    def display_updater(self):
        """Create a string for the updater. This is required to display updater in Admin."""
        return self.updater.get_full_name()

    display_updater.short_description = 'Auteur de la modification'

class NewsDelete(models.Model):
    """
    Intermediate model between "News" and "User", defined to add fields
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='deleted_news')
    deleter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur de la suppression', related_name='news_deleter')
    deletion_date = models.DateTimeField(auto_now=True, verbose_name='Suppression le')
    deletion_reason = models.CharField(blank=False, max_length=250, verbose_name='Raison de la suppression')

    def display_deleter(self):
        """Create a string for the deleter. This is required to display deleter in Admin."""
        return self.deleter.get_full_name()

    display_deleter.short_description = 'Auteur de la suppression'

class Faq(models.Model):
    """
    Model of the "contents_faq" table in the database
    """
    category = models.CharField(max_length=30, choices=FAQ_CATEGORY, default=MISCELLANEOUS, verbose_name='Catégorie')
    question = models.CharField(blank=False, max_length=250, verbose_name='Question')
    answer = models.TextField(blank=False, verbose_name='Réponse')
    status = models.CharField(max_length=30, choices=CONTENT_STATUS, default=ACTIVATED, verbose_name='Statut')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication le')
    photos = models.ManyToManyField(Photo, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_faq')
    
    def __str__(self):
        return f'{self.category} - {self.question}'

    def display_author(self):
        """Create a string for the author. This is required to display author in Admin."""
        return self.author.get_full_name()

    display_author.short_description = 'Auteur'
    
    class Meta:
        verbose_name_plural = "Faqs"
        ordering = ['-creation_date']

class FaqUpdate(models.Model):
    """
    Intermediate model between "Faq" and "User", defined to add fields
    """
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name='updated_faq')
    updater = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='faq_updater')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Modification le')
    update_reason = models.CharField(max_length=250, verbose_name='Raison de la modification')

    def display_updater(self):
        """Create a string for the updater. This is required to display updater in Admin."""
        return self.updater.get_full_name()

    display_updater.short_description = 'Auteur de la modification'

class FaqDelete(models.Model):
    """
    Intermediate model between "Faq" and "User", defined to add fields
    """
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name='deleted_faq')
    deleter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur de la suppression', related_name='faq_deleter')
    deletion_date = models.DateTimeField(auto_now=True, verbose_name='Suppression le')
    deletion_reason = models.CharField(blank=False, max_length=250, verbose_name='Raison de la suppression')

    def display_deleter(self):
        """Create a string for the deleter. This is required to display deleter in Admin."""
        return self.deleter.get_full_name()

    display_deleter.short_description = 'Auteur de la suppression'

class Event(models.Model):
    """
    Model of the "contents_event" table in the database
    """
    category = models.CharField(max_length=30, choices=EVENT_CATEGORY, default=MISCELLANEOUS, verbose_name='Catégorie')
    title = models.CharField(blank=False, max_length=100, verbose_name='Titre')
    content = models.TextField(blank=False, verbose_name='Evènement')
    start_date = models.DateTimeField(verbose_name='Début de l\'évènement')
    end_date = models.DateTimeField(verbose_name='Fin de l\'évènement')
    status = models.CharField(max_length=30, choices=CONTENT_STATUS, default=ACTIVATED, verbose_name='Statut')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication le')
    photos = models.ManyToManyField(Photo, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_events')
    
    def __str__(self):
        return f'Evènement - {self.title}'

    def display_author(self):
        """Create a string for the author. This is required to display author in Admin."""
        return self.author.get_full_name()

    display_author.short_description = 'Auteur'
    
    class Meta:
        verbose_name_plural = "events"

class EventUpdate(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='updated_event')
    updater = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='event_updater')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Modification le')
    update_reason = models.CharField(max_length=250, verbose_name='Raison de la modification')

    def display_updater(self):
        """Create a string for the updater. This is required to display updater in Admin."""
        return self.updater.get_full_name()

    display_updater.short_description = 'Auteur de la modification'

class EventDelete(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='deleted_event')
    deleter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur de la suppression', related_name='event_deleter')
    deletion_date = models.DateTimeField(auto_now=True, verbose_name='Suppression le')
    deletion_reason = models.CharField(blank=False, max_length=250, verbose_name='Raison de la suppression')

    def display_deleter(self):
        """Create a string for the deleter. This is required to display deleter in Admin."""
        return self.deleter.get_full_name()

    display_deleter.short_description = 'Auteur de la suppression'

class Incident(models.Model):
    """
    Model of the "contents_incident" table in the database
    """
    category = models.CharField(max_length=30, choices=INCIDENT_CATEGORY, default=MISCELLANEOUS, verbose_name='Type')
    content = models.TextField(blank=False, verbose_name='Incident')
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

class Comment(models.Model):
    """
    Model of the "contents_comment" table in the database
    """
    content = models.TextField(blank=False, verbose_name='Commentaire')
    status = models.CharField(max_length=30, choices=CONTENT_STATUS, default=ACTIVATED, verbose_name='Statut')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication le')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='add_event_comment')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='add_news_comment')
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='add_incident_comment')
    
    def __str__(self):
        return 'Commentaire de {}'.format(self.user)

    def display_author(self):
        """Create a string for the author. This is required to display author in Admin."""
        return self.author.get_full_name()

    display_author.short_description = 'Auteur'
    
    class Meta:
        verbose_name_plural = "comments"
        ordering = ['-creation_date']

class CommentDelete(models.Model):
    """
    Intermediate model between "Comment" and "User", defined to add fields
    """
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='deleted_comment')
    deleter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur de la suppression', related_name='comment_deleter')
    deletion_date = models.DateTimeField(auto_now=True, verbose_name='Suppression le')
    deletion_reason = models.CharField(blank=False, max_length=250, verbose_name='Raison de la suppression')

    def display_deleter(self):
        """Create a string for the deleter. This is required to display deleter in Admin."""
        return self.deleter.get_full_name()

    display_deleter.short_description = 'Auteur de la suppression'
