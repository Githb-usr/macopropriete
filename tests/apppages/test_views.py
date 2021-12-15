#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import RequestFactory, TestCase
from django.urls import reverse

from config.settings.base import ADMIN_RECIPIENTS
from pages.views import ContactFormView, IndexView

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.contact_url = reverse('contact')
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(
            email='caroline.dupont@free.fr',
            password='fhh456GG455t',
            status='VALIDATED',
            )

        self.mail_no_copy = {
            'first_name': 'Laurent',
            'last_name': 'Dupond',
            'email_address': 'laurent.dupond@gmail.com',
            'user_type': 'OWNER OCCUPIER',
            'message_subject': 'MEETING',
            'cc_myself': 'False',
            'message': 'Lorem ipsum msg1',
        }

        self.mail_with_copy = {
            'first_name': 'Nathalie',
            'last_name': 'Martin',
            'email_address': 'nathalie.martin@hotmail.com',
            'user_type': 'TENANT',
            'message_subject': 'WEBSITE',
            'cc_myself': 'True',
            'message': 'Lorem ipsum msg2',
        }
        
        return super().setUp()

class IndexViewTestCase(BaseTest):
    
    def test_get_context_data(self):
        self.client.force_login(self.user)
        request = self.factory.get('/')
        request.user = self.user
        view = IndexView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('user_uuid', context)
        self.assertEqual(context['user_uuid'], self.user.uuid)

class ContactFormViewTestCase(BaseTest):
    
    def test_form_valid_email(self):
        self.client.force_login(self.user)
        response = self.client.post(self.contact_url, self.mail_no_copy)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, 'parcdelachana@gmail.com')
        self.assertEqual(mail.outbox[0].to, [ADMIN_RECIPIENTS])
        self.assertEqual(mail.outbox[0].subject, 'Parc de La Chana : nouveau message sur le thème "Les réunions"')

    def test_form_valid_email_with_copy(self):
        self.client.force_login(self.user)
        response = self.client.post(self.contact_url, self.mail_with_copy)
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].from_email, 'parcdelachana@gmail.com')
        self.assertEqual(mail.outbox[1].from_email, 'parcdelachana@gmail.com')
        self.assertEqual(mail.outbox[0].to, [ADMIN_RECIPIENTS])
        self.assertEqual(mail.outbox[1].to, ['nathalie.martin@hotmail.com'])
        self.assertEqual(mail.outbox[0].subject, 'Parc de La Chana : nouveau message sur le thème "Le site"')
        self.assertEqual(mail.outbox[1].subject, 'Votre message envoyé au Parc de La Chana sur le thème "Le site"')
