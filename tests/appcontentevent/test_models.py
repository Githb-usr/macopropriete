#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase

from contentevent.models import Event, EventUpdate, EventDelete

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

        self.event1 = Event.objects.create(
            category='MEETING',
            title='Titre event 1',
            content='Lorem ipsum event',
            start_date='2021-11-25 08:00:00+01',
            end_date='2021-11-25 09:00:00+01',
            status='ACTIVATED',
            author=self.user1,
        )

        self.event_update1 = EventUpdate.objects.create(
            event=self.event1,
            updater=self.user1,
            update_reason='Lorem ipsum event update',
        )

        self.event_delete1 = EventDelete.objects.create(
            event=self.event1,
            deleter=self.user2,
            deletion_reason='Lorem ipsum event delete',
        )

        return super().setUp()

class EventModelTestCase(BaseTest):

    def test_object_name(self):
        event = Event.objects.get(id=self.event1.pk)
        expected_object_name = f'Evènement - {event.title}'
        self.assertEquals(expected_object_name, str(event))

    def test_display_author(self):
        event = Event.objects.get(id=self.event1.pk)
        expected_author_name = event.display_author()
        self.assertEquals(expected_author_name, 'Nicolas Martin')

class EventUpdateModelTestCase(BaseTest):

    def test_display_updater(self):
        event_update = EventUpdate.objects.get(id=self.event_update1.pk)
        expected_updater_name = event_update.display_updater()
        self.assertEquals(expected_updater_name, 'Nicolas Martin')

class EventDeleteModelTestCase(BaseTest):

    def test_display_deleter(self):
        event_delete = EventDelete.objects.get(id=self.event_delete1.pk)
        expected_deleter_name = event_delete.display_deleter()
        self.assertEquals(expected_deleter_name, 'Valérie Plouf')
