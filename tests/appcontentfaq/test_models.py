#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase

from contentfaq.models import Faq, FaqUpdate, FaqDelete

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

        self.faq1 = Faq.objects.create(
            category='MEETING',
            question='Titre faq 1',
            answer='Lorem ipsum Faq',
            status='ACTIVATED',
            author=self.user1,
        )

        self.faq_update1 = FaqUpdate.objects.create(
            faq=self.faq1,
            updater=self.user1,
            update_reason='Lorem ipsum Faq update',
        )

        self.faq_delete1 = FaqDelete.objects.create(
            faq=self.faq1,
            deleter=self.user2,
            deletion_reason='Lorem ipsum Faq delete',
        )

        return super().setUp()

class FaqModelTestCase(BaseTest):

    def test_object_name(self):
        faq = Faq.objects.get(id=self.faq1.pk)
        expected_object_name = f'{faq.category} - {faq.question}'
        self.assertEquals(expected_object_name, str(faq))

    def test_display_author(self):
        faq = Faq.objects.get(id=self.faq1.pk)
        expected_author_name = faq.display_author()
        self.assertEquals(expected_author_name, 'Nicolas Martin')

class FaqUpdateModelTestCase(BaseTest):

    def test_display_updater(self):
        faq_update = FaqUpdate.objects.get(id=self.faq_update1.pk)
        expected_updater_name = faq_update.display_updater()
        self.assertEquals(expected_updater_name, 'Nicolas Martin')

class FaqDeleteModelTestCase(BaseTest):

    def test_display_deleter(self):
        faq_delete = FaqDelete.objects.get(id=self.faq_delete1.pk)
        expected_deleter_name = faq_delete.display_deleter()
        self.assertEquals(expected_deleter_name, 'Valérie Plouf')
