#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import reverse

from contentfaq.models import Faq
from contentfaq.settings import QUESTION_CREATION_SUCCESS,\
    QUESTION_DELETE_SUCCESS, QUESTION_UPDATE_SUCCESS
from contentfaq.views import FaqCategoryView

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.faq_create_view_url = reverse('faq-create')
        self.view = FaqCategoryView()
        
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

        self.faq1 = Faq.objects.create(
            category='BUILDINGS',
            question='FAQ 1',
            answer='Lorem ipsum FAQ1',
            author=self.user1
            )

        self.faq2 = Faq.objects.create(
            category='BUILDINGS',
            question='FAQ 2',
            answer='Lorem ipsum FAQ2',
            author=self.user1
            )

        self.faq3 = Faq.objects.create(
            category='BUILDINGS',
            question='FAQ 3',
            answer='Lorem ipsum FAQ3',
            author=self.user2
            )

        self.faq4_data_ok = {
            'category': 'BUILDINGS',
            'question': 'FAQ 4',
            'answer': 'Lorem ipsum FAQ4',
            'author': self.user2
        }

        self.faq2_data_update = {
            'category': 'BUILDINGS',
            'question': 'FAQ 2 update',
            'answer': 'Lorem ipsum FAQ2 update',
            'author': self.user1,
            'update_reason': 'FAQ 2 update reason',
            'updater': self.user2,
        }

        self.faq3_delete = {
            'deletion_reason': 'FAQ 3 delete reason',
            'deleter': self.user2,
        }

        return super().setUp()

class FaqCategoryViewTestCase(BaseTest):

    def test_get_context_data(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('faq-category', args=(self.faq1.category,)))
        context = response.context
        self.assertIn('current_category', context)
        self.assertIn('page_range_top', context)
        self.assertIn('page_range_bottom', context)

class FaqCreateViewTestCase(BaseTest):

    def test_faq_create_view_post_valid_form(self):
        self.client.force_login(self.user2)
        form_data = self.faq4_data_ok
        response = self.client.post(self.faq_create_view_url, data=form_data)
        faq4 = Faq.objects.get(question='FAQ 4')
        self.assertEqual(faq4.answer, 'Lorem ipsum FAQ4')
        self.assertEqual(faq4.author, self.user2)
        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), QUESTION_CREATION_SUCCESS)
        # test redirection
        self.assertEqual(response.status_code, 302)
        url_part = faq4.category.lower()
        self.assertEqual(response['location'], f'/faq/{url_part}')

    def test_faq_create_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('faq-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Créer une question')

class FaqUpdateViewTestCase(BaseTest):

    def test_faq_update_view_post_valid_form(self):
        self.client.force_login(self.user2)
        faq_update_url = reverse('faq-update', args=(self.faq2.uuid,))
        form_data = self.faq2_data_update
        response = self.client.post(faq_update_url, data=form_data)
        faq2_up = Faq.objects.get(uuid=self.faq2.uuid)
        # Test question after update
        self.assertEqual(faq2_up.question, 'FAQ 2 update')
        self.assertEqual(faq2_up.updated_faq.first().updater, self.user2)
        self.assertEqual(faq2_up.updated_faq.first().update_reason, 'FAQ 2 update reason')
        # Test message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), QUESTION_UPDATE_SUCCESS)

    def test_faq_update_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('faq-update', args=(self.faq2.uuid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Modifier la question')

class FaqDeleteViewTestCase(BaseTest):

    def test_faq_delete_view_post_valid_form(self):
        self.client.force_login(self.user1)
        faq_delete_url = reverse('faq-delete', args=(self.faq3.uuid,))
        form_data = self.faq3_delete
        response = self.client.post(faq_delete_url, data=form_data)
        faq3_del = Faq.objects.get(uuid=self.faq3.uuid)
        # Test question after delete
        self.assertEqual(faq3_del.status, 'DELETED')
        self.assertEqual(faq3_del.deleted_faq.first().deleter, self.user1)
        self.assertEqual(faq3_del.deleted_faq.first().deletion_reason, 'FAQ 3 delete reason')
        # Test message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), QUESTION_DELETE_SUCCESS)

    def test_faq_delete_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('faq-delete', args=(self.faq3.uuid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Supprimer la question')
