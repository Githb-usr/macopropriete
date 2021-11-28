#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ckeditor_uploader.fields import RichTextUploadingField 
from django.db import models
from django.urls import reverse
import uuid

from contentnews.settings import ACTIVATED, NEWS_CATEGORY, MISCELLANEOUS, STATUS
from config.settings.base import AUTH_USER_MODEL

class News(models.Model):
    """
    Model of the "contents_news" table in the database
    """
    category = models.CharField(max_length=30, choices=NEWS_CATEGORY, default=MISCELLANEOUS, verbose_name='Catégorie')
    title = models.CharField(blank=False, max_length=100, verbose_name='Titre')
    content = RichTextUploadingField(blank=False, verbose_name='News')
    status = models.CharField(max_length=30, choices=STATUS, default=ACTIVATED, verbose_name='Statut')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication le')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Auteur', related_name='create_news')

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
