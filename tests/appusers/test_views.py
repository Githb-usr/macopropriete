#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.settings import ACCOUNT_DOES_NOT_EXIST, ALREADY_VALIDATED_ACCOUNT_MSG,\
    VALIDATED_ACCOUNT_SUCCESS_MSG

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.no_user_uuid = '9638abfb-8aa0-482f-8850-2d8d8f0f275f'
        
        User = get_user_model()
        self.user1 = User.objects.create_user(
            email='nicolas.martin@free.fr',
            )

        self.user2 = User.objects.create_user(
            email='caroline.dupont@free.fr',
            password='fhh456GG455t',
            status='VALIDATED',
            )
        
        return super().setUp()

class ValidateUserAccountViewTestCase(BaseTest):

    def assert_model(self, response, msg):
        # test messages without context
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), msg)
        # test redirection
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/login/')

    def test_validate_user_account_view_user_ok(self):
        response = self.client.get(reverse('account-validation', args=(self.user1.uuid,)))
        self.assert_model(response, VALIDATED_ACCOUNT_SUCCESS_MSG)

    def test_validate_user_account_view_user_already_validated(self):
        response = self.client.get(reverse('account-validation', args=(self.user2.uuid,)))
        self.assert_model(response, ALREADY_VALIDATED_ACCOUNT_MSG)

    def test_validate_user_account_view_no_user(self):
        response = self.client.get(reverse('account-validation', args=(self.no_user_uuid,)))
        self.assert_model(response, ACCOUNT_DOES_NOT_EXIST)

class ProfileViewTestCase(BaseTest):

    def test_get_context_data(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('profile', args=(self.user2.uuid,)))
        context = response.context
        self.assertIn('uuid', context)
        self.assertEqual(response.context['uuid'], self.user2.uuid)
