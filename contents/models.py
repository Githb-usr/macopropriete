#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
import uuid

class Article(models.Model):
    """
    Model of the "contents_article" table in the database
    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    CONDOMINIUM = 'Condominium'
    MEETING = 'Meeting'
    MISCELLANEOUS='Miscellaneous'
    WEBSITE = 'Website'
    WORKS = 'Works'
    ARTICLE_CATEGORY = [
        (CONDOMINIUM, 'Copropriété'),
        (MEETING, 'Réunion'),
        (WEBSITE, 'Site'),
        (WORKS, 'Travaux'),
        (MISCELLANEOUS, 'Divers'),
    ]
    category = models.CharField(max_length=30, choices=ARTICLE_CATEGORY, default=MISCELLANEOUS)
    title = models.CharField(blank=False, max_length=100, verbose_name='Titre')
    content = models.TextField(blank=False, verbose_name='Article')
    image = models.ImageField(upload_to='contents')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication de l\'article')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_article')
    # article status
    ACTIVATED = 'Activated'
    DELETED = 'Deleted'
    ARTICLE_STATUS = [
        (ACTIVATED, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=ARTICLE_STATUS, default=ACTIVATED)
        
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = "articles"
        ordering = ['-creation_date']

class ArticleUpdate(models.Model):
    """
    Intermediate model between "Article" and "User", defined to add fields
    """
    updater = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='article_updater')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='updated_article')
    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de la modification')
    update_reason = models.CharField(max_length=250, verbose_name='Motif de la modification')

class ArticleDelete(models.Model):
    """
    Intermediate model between "Article" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='article_deleter')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='deleted_article')
    delete_date = models.DateTimeField(auto_now=True, null=True)
    delete_reason = models.CharField(max_length=250, null=False)

class Faq(models.Model):
    """
    Model of the "contents_faq" table in the database
    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    BUILDINGS = 'Buildings'
    CAR_PARKS = 'Car parks'
    INDIVIDUAL_GARAGES = 'Individual garages'
    MISCELLANEOUS='Miscellaneous'
    PARK = 'Park'
    FAQ_CATEGORY = [
        (BUILDINGS, 'Les bâtiments'),
        (INDIVIDUAL_GARAGES, 'Les garages'),
        (PARK, 'Le parc'),
        (CAR_PARKS, 'Les parkings'),
        (MISCELLANEOUS, 'Divers'),
    ]
    category = models.CharField(max_length=30, choices=FAQ_CATEGORY, default=MISCELLANEOUS)
    question = models.CharField(blank=False, max_length=250, verbose_name='Question')
    answer = models.TextField(blank=False, verbose_name='Réponse')
    image = models.ImageField(upload_to='contents/faqs/')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication de la question')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_faq')
    # FAQ status
    ACTIVATED = 'Activated'
    DELETED = 'Deleted'
    FAQ_STATUS = [
        (ACTIVATED, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=FAQ_STATUS, default=ACTIVATED)
    
    def __str__(self):
        return f'{self.faq_section} - {self.question}'
    
    class Meta:
        verbose_name_plural = "Faqs"

class FaqUpdate(models.Model):
    """
    Intermediate model between "Faq" and "User", defined to add fields
    """
    updater = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='faq_updater')
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name='updated_faq')
    update_date = models.DateTimeField(auto_now=True, null=True)
    update_reason = models.CharField(max_length=250)

class FaqDelete(models.Model):
    """
    Intermediate model between "Faq" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='faq_deleter')
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name='deleted_faq')
    delete_date = models.DateTimeField(auto_now=True, null=True)
    delete_reason = models.CharField(max_length=250, null=False)

class Event(models.Model):
    """
    Model of the "contents_event" table in the database
    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    PARTY = 'Party'
    MEETING = 'Meeting'
    MISCELLANEOUS='Miscellaneous'
    WEBSITE = 'Website'
    WORKS = 'Works'
    EVENT_CATEGORY = [
        (PARTY, 'Fête'),
        (WEBSITE, 'Site'),
        (MEETING, 'Réunion'),
        (WORKS, 'Travaux'),
        (MISCELLANEOUS, 'Divers'),
    ]
    category = models.CharField(max_length=30, choices=EVENT_CATEGORY, default=MISCELLANEOUS)
    title = models.CharField(blank=False, max_length=100, verbose_name='Titre')
    content = models.TextField(blank=False, verbose_name='Evènement')
    image = models.ImageField(upload_to='contents/events/')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication de l\'évènement')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    start_date = models.DateTimeField(verbose_name='Début de l\'évènement')
    end_date = models.DateTimeField(verbose_name='Fin de l\'évènement')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_events')
    # Event status
    ACTIVATED = 'Activated'
    DELETED = 'Deleted'
    EVENT_STATUS = [
        (ACTIVATED, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=EVENT_STATUS, default=ACTIVATED)
    
    def __str__(self):
        return f'Evènement - {self.title}'
    
    class Meta:
        verbose_name_plural = "events"

class EventUpdate(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    updater = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='event_updater')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='updated_event')
    update_date = models.DateTimeField(auto_now=True, null=True)
    update_reason = models.CharField(max_length=250)

class EventDelete(models.Model):
    """
    Intermediate model between "Event" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='event_deleter')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='deleted_event')
    delete_date = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de suppression')
    delete_reason = models.CharField(max_length=250, null=False, verbose_name='Motif de la suppression')

class Incident(models.Model):
    """
    Model of the "contents_incident" table in the database
    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    ACCIDENT = 'Accident'
    BREAKDOWN = 'Breakdown'
    DAMAGE = 'Damage'
    MISCELLANEOUS='Miscellaneous'
    WATER_LEAKAGE = 'Water leakage'
    INCIDENT_CATEGORY = [
        (ACCIDENT, 'Accident'),
        (DAMAGE, 'Dégradation'),
        (WATER_LEAKAGE, 'Fuite d\'eau'),
        (BREAKDOWN, 'Panne'),        
        (MISCELLANEOUS, 'Divers'),
    ]
    category = models.CharField(max_length=30, choices=INCIDENT_CATEGORY, default=MISCELLANEOUS, verbose_name='Type d\'incident')
    zone = models.ForeignKey('condominium.Zone', on_delete=models.CASCADE, related_name='incident_zone')
    content = models.TextField(blank=False, verbose_name='Incident')
    image = models.ImageField(upload_to='contents/incidents/')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication de l\'incident')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Déclarant', related_name='create_incident')
    
    def __str__(self):
        return f'Incident - {self.incident_type}'
    
    class Meta:
        verbose_name_plural = "incidents"

class IncidentDelete(models.Model):
    """
    Intermediate model between "Incident" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='incident_deleter')
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='deleted_incident')
    delete_date = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de suppression')
    delete_reason = models.CharField(max_length=250, null=False, verbose_name='Motif de la suppression')

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
    status = models.CharField(max_length=20, choices=TRACKING_STATUS, default=PENDING)
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
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    content = models.TextField(blank=False, verbose_name='Commentaire')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication du commentaire')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='add_comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='add_comments')
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='add_comments')
    # article status
    ACTIVATED = 'Activated'
    DELETED = 'Deleted'
    COMMENT_STATUS = [
        (ACTIVATED, 'Actif'),
        (DELETED, 'Supprimé'),
    ]
    status = models.CharField(max_length=30, choices=COMMENT_STATUS, default=ACTIVATED)
    
    def __str__(self):
        return 'Commentaire de {}'.format(self.user)
    
    class Meta:
        verbose_name_plural = "comments"
        ordering = ['-creation_date']

class CommentDelete(models.Model):
    """
    Intermediate model between "Comment" and "User", defined to add fields
    """
    deleter = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Auteur', related_name='comment_deleter')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='deleted_comment')
    delete_date = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de suppression')
    delete_reason = models.CharField(max_length=250, null=False, verbose_name='Motif de la suppression')
