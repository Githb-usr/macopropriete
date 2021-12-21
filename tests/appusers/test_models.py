#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.models import User

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
            email='caroline.dupont@free.fr',
        )

        return super().setUp()

class UserManagerTestCase(BaseTest):
    def test_create_user_ok(self):
        test_user = get_user_model().objects.create_user(
            email='user@test.com',
            first_name='Laurent',
            last_name='Dupont',
            password='fhh456GG455t'
        )
        self.assertEqual(test_user.email, 'user@test.com')
        self.assertEqual(test_user.first_name, 'Laurent')
        self.assertEqual(test_user.last_name, 'Dupont')
        self.assertTrue(test_user.check_password('fhh456GG455t'))
        self.assertEqual(test_user.status, 'PENDING')
        self.assertFalse(test_user.is_staff)
        self.assertFalse(test_user.is_superuser)
        self.assertTrue(test_user.is_active)

    def test_create_superuser_ok(self):
        test_superuser = get_user_model().objects.create_superuser(
            email='superuser@test.com',
            first_name='Fabrice',
            last_name='Dupin',
            password='fhh456GG455t'
        )
        self.assertEqual(test_superuser.email, 'superuser@test.com')
        self.assertEqual(test_superuser.first_name, 'Fabrice')
        self.assertEqual(test_superuser.last_name, 'Dupin')
        self.assertTrue(test_superuser.check_password('fhh456GG455t'))
        self.assertEqual(test_superuser.status, 'VALIDATED')
        self.assertTrue(test_superuser.is_staff)
        self.assertTrue(test_superuser.is_superuser)
        self.assertTrue(test_superuser.is_active)

    def test_create_superuser_isstaff_false(self):
        with self.assertRaises(ValueError) as cm:
            get_user_model().objects.create_superuser(
                email='superuser@test.com',
                password='fhh456GG455t',
                is_staff=False,
                is_superuser=False,
            )
        is_staff_error = cm.exception
        self.assertEqual(str(is_staff_error), 'Un super utilisateur doit avoir is_staff=True.')

    def test_create_superuser_issuperuser_false(self):
        with self.assertRaises(ValueError) as cm:
            get_user_model().objects.create_superuser(
                email='superuser@test.com',
                password='fhh456GG455t',
                is_superuser=False,
            )
        is_superuser_error = cm.exception
        self.assertEqual(str(is_superuser_error), 'Un super utilisateur doit avoir is_superuser=True.')

class UserModelTestCase(BaseTest):

    def test_object_name_is_email(self):
        user = User.objects.get(id=self.user1.pk)
        expected_object_name = user.email
        self.assertEquals(expected_object_name, str(user))

    def test_get_full_name(self):
        user = User.objects.get(id=self.user1.pk)
        expected_full_name = f'{user.first_name} {user.last_name}'
        self.assertEquals(expected_full_name, user.get_full_name())

    def test_get_full_name_mail_only(self):
        user = User.objects.get(id=self.user2.pk)
        expected_full_name = 'Caroline.dupont'
        self.assertEquals(expected_full_name, user.get_full_name())

    def test_get_absolute_url(self):
        user = User.objects.get(id=self.user1.pk)
        expected_absolute_url = reverse('profile', kwargs={'uuid': self.user1.uuid})
        self.assertEquals(expected_absolute_url, user.get_absolute_url())
