#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import RequestFactory, TestCase
from django.urls import reverse

from contentnews.models import News
from contentnews.settings import NEWS_CREATION_SUCCESS, NEWS_DELETE_SUCCESS,\
    NEWS_UPDATE_SUCCESS
from contentnews.views import NewsListView

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.news_create_view_url = reverse('news-create')
        User = get_user_model()
        self.user1 = User.objects.create_user(
            email='caroline.dupont@free.fr',
            password='fhh456GG455t',
            status='VALIDATED',
            )

        self.user2 = User.objects.create_user(
            email='nicolas.martin@free.fr',
            password='265fj1fdhj5fj',
            status='VALIDATED',
            )

        self.news_data_ok = {
            'category': 'WORKS',
            'title': 'News 4',
            'content': 'Lorem ipsum news4',
            'status': 'ACTIVATED',
            'author': self.user2
        }

        self.news_data_error = {
            'category': 'MEETING',
            'title': '',
            'content': 'Lorem ipsum news5',
            'status': 'ACTIVATED',
            'author': self.user2
        }

        self.news1_data_update = {
            'category': 'MEETING',
            'title': 'News 1 update',
            'content': 'Lorem ipsum news1 update',
            'status': 'ACTIVATED',
            'author': self.user1,
            'update_reason': 'News 1 update reason',
            'updater': self.user2,
        }

        self.news2_delete = {
            'deletion_reason': 'News 2 delete reason',
            'deleter': self.user2,
        }

        return super().setUp()

    def create_test_news(self):
        self.news1 = News.objects.create(
            category='MEETING',
            title='News 1',
            content='Lorem ipsum news1',
            status='ACTIVATED',
            author=self.user1
            )

        self.news2 = News.objects.create(
            category='WEBSITE',
            title='News 2',
            content='Lorem ipsum news2',
            status='ACTIVATED',
            author=self.user1
            )

        self.news3 = News.objects.create(
            category='CONDOMINIUM',
            title='News 3',
            content='Lorem ipsum news3',
            status='ACTIVATED',
            author=self.user2
            )

    def delete_all_news(self):
        self.news1 = News.objects.update_or_create(status='DELETED', author=self.user1)
        self.news2 = News.objects.update_or_create(status='DELETED', author=self.user1)
        self.news3 = News.objects.update_or_create(status='DELETED', author=self.user2)

class NewsListViewTestCase(BaseTest):
    
    def test_get_queryset(self):
        self.create_test_news()
        self.client.force_login(self.user2)
        request = RequestFactory().get('news/')
        view = NewsListView()
        view.request = request
        self.assertQuerysetEqual(view.get_queryset(), News.objects.filter(status='ACTIVATED'))
        self.assertEqual(len(News.objects.filter(status='ACTIVATED')), 3)

    def test_get_context_data(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('news-list'))
        context = response.context
        self.assertIn('page_range_top', context)
        self.assertIn('page_range_bottom', context)

class NewsCreateViewTestCase(BaseTest):

    def test_news_create_view_post_valid_form(self):
        self.client.force_login(self.user2)
        form_data = self.news_data_ok
        response = self.client.post(self.news_create_view_url, data=form_data)
        news4 = News.objects.get(title='News 4')
        self.assertEqual(news4.content, 'Lorem ipsum news4')
        self.assertEqual(news4.author, self.user2)
        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), NEWS_CREATION_SUCCESS)
        # test redirection
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], f'/news/{news4.uuid}/')

    def test_news_create_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('news-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Créer une news')

class NewsUpdateViewTestCase(BaseTest):

    def test_news_update_view_post_valid_form(self):
        self.client.force_login(self.user2)
        self.create_test_news()
        news_update_url = reverse('news-update', args=(self.news1.uuid,))
        form_data = self.news1_data_update
        response = self.client.post(news_update_url, data=form_data)
        news1_up = News.objects.get(uuid=self.news1.uuid)
        # Test news after update
        self.assertEqual(news1_up.title, 'News 1 update')
        self.assertEqual(news1_up.updated_news.first().updater, self.user2)
        self.assertEqual(news1_up.updated_news.first().update_reason, 'News 1 update reason')
        # Test message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), NEWS_UPDATE_SUCCESS)

    def test_news_update_view_get(self):
        self.client.force_login(self.user2)
        self.create_test_news()
        response = self.client.get(reverse('news-update', args=(self.news1.uuid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Modifier la news')

class NewsDeleteViewTestCase(BaseTest):

    def test_news_delete_view_post_valid_form(self):
        self.client.force_login(self.user2)
        self.create_test_news()
        news_delete_url = reverse('news-delete', args=(self.news2.uuid,))
        form_data = self.news2_delete
        response = self.client.post(news_delete_url, data=form_data)
        news2 = News.objects.get(uuid=self.news2.uuid)
        # Test news after delete
        self.assertEqual(news2.status, 'DELETED')
        self.assertEqual(news2.deleted_news.first().deleter, self.user2)
        self.assertEqual(news2.deleted_news.first().deletion_reason, 'News 2 delete reason')
        # Test message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), NEWS_DELETE_SUCCESS)

    def test_news_delete_view_get(self):
        self.client.force_login(self.user2)
        self.create_test_news()
        response = self.client.get(reverse('news-delete', args=(self.news1.uuid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Supprimer la news')
