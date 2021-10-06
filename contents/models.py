#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.urls import reverse

class Article(models.Model):
    """
    Model of the "contents_article" table in the database
    """
    title = models.CharField(blank=False, max_length=100)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='contents/articles/')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Création de l\'article')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='create_article')
    # article status
    ACTIVE = 'Active'
    DELETED = 'Deleted'
    ARTICLE_STATUS = [
        (ACTIVE, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=ARTICLE_STATUS)
        
    def __str__(self):
        return f'{self.article_type} - {self.title}'
    
    class Meta:
        verbose_name_plural = "articles"

class ArticleUpdate(models.Model):
    """
    Intermediate model between "Article" and "User", defined to add fields
    """
    updater = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='article_updater')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='updated_article')
    update_date = models.DateTimeField(auto_now=True, null=True)
    update_reason = models.CharField(max_length=250)

class ArticleDelete(models.Model):
    """
    Intermediate model between "Article" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='article_deleter')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='deleted_article')
    delete_date = models.DateTimeField(auto_now=True, null=True)
    delete_reason = models.CharField(max_length=250, null=False)

class Faq(models.Model):
    """
    Model of the "contents_faq" table in the database
    """
    faq_section = models.CharField(max_length=30)
    question = models.CharField(blank=False, max_length=250)
    answer = models.TextField(blank=False)
    image = models.ImageField(upload_to='contents/faqs/')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Création de la question')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='create_faq')
    # FAQ status
    ACTIVE = 'Active'
    DELETED = 'Deleted'
    FAQ_STATUS = [
        (ACTIVE, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=FAQ_STATUS)
    
    def __str__(self):
        return f'{self.faq_section} - {self.question}'
    
    class Meta:
        verbose_name_plural = "Faqs"

class FaqUpdate(models.Model):
    """
    Intermediate model between "Faq" and "User", defined to add fields
    """
    updater = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='faq_updater')
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name='updated_faq')
    update_date = models.DateTimeField(auto_now=True, null=True)
    update_reason = models.CharField(max_length=250)

class FaqDelete(models.Model):
    """
    Intermediate model between "Faq" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='faq_deleter')
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name='deleted_faq')
    delete_date = models.DateTimeField(auto_now=True, null=True)
    delete_reason = models.CharField(max_length=250, null=False)

class Event(models.Model):
    """
    Model of the "contents_event" table in the database
    """
    title = models.CharField(blank=False, max_length=100)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='contents/events/')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Création de l\'évènement')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    start_date = models.DateTimeField(verbose_name='Début de l\'évènement')
    end_date = models.DateTimeField(verbose_name='Fin de l\'évènement')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='create_events')
    # Event status
    ACTIVE = 'Active'
    DELETED = 'Deleted'
    EVENT_STATUS = [
        (ACTIVE, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=EVENT_STATUS)
    
    def __str__(self):
        return f'Evènement - {self.title}'
    
    class Meta:
        verbose_name_plural = "events"

class EventUpdate(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    updater = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='event_updater')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='updated_event')
    update_date = models.DateTimeField(auto_now=True, null=True)
    update_reason = models.CharField(max_length=250)

class EventDelete(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='event_deleter')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='deleted_event')
    delete_date = models.DateTimeField(auto_now=True, null=True)
    delete_reason = models.CharField(max_length=250, null=False)

class Incident(models.Model):
    """
    Model of the "contents_incident" table in the database
    """
    incident_type = models.CharField(max_length=30)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='contents/incidents/')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Création de l\'incident')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='create_incident')
    zone = models.ForeignKey('condominium.Zone', on_delete=models.CASCADE, related_name='incident_zone')
    
    def __str__(self):
        return f'Incident - {self.incident_type}'
    
    class Meta:
        verbose_name_plural = "incidents"

class IncidentDelete(models.Model):
    """
    Intermediate model between "Incident" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='incident_deleter')
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='deleted_incident')
    delete_date = models.DateTimeField(auto_now=True, null=True)
    delete_reason = models.CharField(max_length=250, null=False)

class IncidentTracking(models.Model):
    """
    Model of the "contents_incidentTracking" table in the database
    """
    # incident status
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    REGISTERED = 'Registered'
    IN_PROGRESS = 'In progress'
    CLOSED = 'Closed'
    TRACKING_STATUS = [
        (PENDING, 'en attente'),
        (REJECTED, 'rejeté'),
        (REGISTERED, 'enregistré'),
        (IN_PROGRESS, 'en cours'),
        (CLOSED, 'fermé'),
    ]
    status = models.CharField(max_length=20, choices=TRACKING_STATUS)
    status_date = models.DateTimeField(auto_now=True)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='incident')
    
    def __str__(self):
        return status
    
    class Meta:
        verbose_name_plural = "Incident status"

class Comment(models.Model):
    """
    Model of the "contents_comment" table in the database
    """
    content = models.TextField(blank=False, verbose_name='')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Création du commentaire')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='create_comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='add_comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='add_comments')
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='add_comments')
    # article status
    ACTIVE = 'Active'
    DELETED = 'Deleted'
    COMMENT_STATUS = [
        (ACTIVE, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=COMMENT_STATUS)
    
    def __str__(self):
        return 'Commentaire de {}'.format(self.user)
    
    class Meta:
        verbose_name_plural = "comments"
        ordering = ['-creation_date']

class CommentDelete(models.Model):
    """
    Intermediate model between "Comment" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comment_deleter')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='deleted_comment')
    delete_date = models.DateTimeField(auto_now=True, null=True)
    delete_reason = models.CharField(max_length=250, null=False)
