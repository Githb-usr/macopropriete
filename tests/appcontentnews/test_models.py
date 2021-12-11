#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from contentnews.models import News, NewsUpdate, NewsDelete

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        self.user1 = User.objects.create_user(
            email='nicolas.martin@free.fr',
            first_name='Nicolas',
            last_name='Martin',
            )

        self.user2 = User.objects.create_user(
            email='valerie.plouf@hop.com',
            first_name='Valérie',
            last_name='Plouf',
            )

        self.news1 = News.objects.create(
            category='MEETING',
            title='Titre news 1',
            content='Lorem ipsum news',
            status='ACTIVATED',
            author=self.user1,
            )

        self.news_update1 = NewsUpdate.objects.create(
            news=self.news1,
            updater=self.user1,
            update_reason='Lorem ipsum news update',
            )

        self.news_delete1 = NewsDelete.objects.create(
            news=self.news1,
            deleter=self.user2,
            deletion_reason='Lorem ipsum news delete',
            )

        return super().setUp()
    
class NewsModelTestCase(BaseTest):

    def test_object_name(self):
        news = News.objects.get(id=self.news1.pk)
        expected_object_name = news.title
        self.assertEquals(expected_object_name, str(news))

    def test_get_absolute_url(self):
        news = News.objects.get(id=self.news1.pk)
        expected_absolute_url = reverse('news-detail', kwargs={'uuid': news.uuid})
        self.assertEquals(expected_absolute_url, news.get_absolute_url())

    def test_display_author(self):
        news = News.objects.get(id=self.news1.pk)
        expected_author_name = news.display_author()
        self.assertEquals(expected_author_name, 'Nicolas Martin')

class NewsUpdateModelTestCase(BaseTest):

    def test_display_updater(self):
        news_update = NewsUpdate.objects.get(id=self.news_update1.pk)
        expected_updater_name = news_update.display_updater()
        self.assertEquals(expected_updater_name, 'Nicolas Martin')

class NewsDeleteModelTestCase(BaseTest):

    def test_display_deleter(self):
        news_delete = NewsDelete.objects.get(id=self.news_delete1.pk)
        expected_deleter_name = news_delete.display_deleter()
        self.assertEquals(expected_deleter_name, 'Valérie Plouf')
