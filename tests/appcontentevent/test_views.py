#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils import timezone

from contentevent.models import Event
from contentevent.settings import EVENT_CREATION_SUCCESS, EVENT_DELETE_SUCCESS,\
    EVENT_UPDATE_SUCCESS
from contentevent.views import EventListNewView, EventListOldView

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.event_create_view_url = reverse('event-create')
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

        self.event1 = Event.objects.create(
            category='MEETING',
            title='Event 1',
            content='Lorem ipsum event1',
            start_date='2021-09-28 09:00:00+01',
            end_date='2021-09-28 12:00:00+01',
            status='ACTIVATED',
            author=self.user1
            )

        self.event2 = Event.objects.create(
            category='WEBSITE',
            title='Event 2',
            content='Lorem ipsum event2',
            start_date='2021-10-05 12:30:00+01',
            end_date='2021-10-05 14:30:00+01',
            status='ACTIVATED',
            author=self.user1
            )

        self.event3 = Event.objects.create(
            category='CONDOMINIUM',
            title='Event 3',
            content='Lorem ipsum event3',
            start_date='2021-11-11 18:00:00+01',
            end_date='2021-11-12 10:00:00+01',
            status='ACTIVATED',
            author=self.user2
            )

        self.event4 = Event.objects.create(
            category='MEETING',
            title='Event 4',
            content='Lorem ipsum event4',
            start_date='2022-01-28 09:00:00+01',
            end_date='2022-01-28 12:00:00+01',
            status='ACTIVATED',
            author=self.user1
            )

        self.event5 = Event.objects.create(
            category='WEBSITE',
            title='Event 5',
            content='Lorem ipsum event5',
            start_date='2022-02-05 12:30:00+01',
            end_date='2022-02-05 14:30:00+01',
            status='ACTIVATED',
            author=self.user1
            )

        self.event6 = Event.objects.create(
            category='CONDOMINIUM',
            title='Event 6',
            content='Lorem ipsum event6',
            start_date='2022-03-11 18:00:00+01',
            end_date='2022-03-12 10:00:00+01',
            status='ACTIVATED',
            author=self.user2
            )

        self.event7_data_ok = {
            'category': 'WORKS',
            'title': 'Event 7',
            'content': 'Lorem ipsum event7',
            # Split datetime into date and time because of the SplitDateTimeWidget
            'start_date_0': '2022-01-02',
            'start_date_1': '18:00',
            'end_date_0': '2022-01-03',
            'end_date_1': '10:00',
            'author': self.user2
        }

        self.event4_data_update = {
            'category': 'MEETING',
            'title': 'Event 4 update',
            'content': 'Lorem ipsum event4 update',
            'start_date_0': '2022-01-28',
            'start_date_1': '09:00',
            'end_date_0': '2022-01-28',
            'end_date_1': '12:00',
            'author': self.user1,
            'update_reason': 'Event 4 update reason',
            'updater': self.user2,
        }

        self.event6_delete = {
            'deletion_reason': 'Event 6 delete reason',
            'deleter': self.user2,
        }

        self.event3_delete = {
            'deletion_reason': 'Event 3 delete reason',
            'deleter': self.user1,
        }

        return super().setUp()

class EventListNewViewTestCase(BaseTest):

    def test_get_queryset(self):
        self.client.force_login(self.user2)
        request = RequestFactory().get('events/')
        view = EventListNewView()
        view.request = request
        current_datetime = timezone.now()
        test_request = Event.objects.filter(start_date__gt=current_datetime).filter(status='ACTIVATED').order_by('start_date')
        self.assertQuerysetEqual(view.get_queryset(), test_request)
        self.assertEqual(len(test_request), 3)
    
    def test_get_context_data(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('event-list-new'))
        context = response.context
        self.assertIn('page_range_top', context)
        self.assertIn('page_range_bottom', context)

class EventListOldViewTestCase(BaseTest):

    def test_get_queryset(self):
        self.client.force_login(self.user2)
        request = RequestFactory().get('events/ended')
        view = EventListOldView()
        view.request = request
        current_datetime = timezone.now()
        test_request = Event.objects.filter(start_date__lt=current_datetime).filter(status='ACTIVATED').order_by('-start_date')
        self.assertQuerysetEqual(view.get_queryset(), test_request)
        self.assertEqual(len(test_request), 3)
    
    def test_get_context_data(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('event-list-old'))
        context = response.context
        self.assertIn('page_range_top', context)
        self.assertIn('page_range_bottom', context)

class EventDetailViewTestCase(BaseTest):

    def test_get_context_data(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('event-detail', args=(self.event1.uuid,)))
        context = response.context
        self.assertIn('now', context)

class EventCreateViewTestCase(BaseTest):

    def test_event_create_view_post_valid_form(self):
        self.client.force_login(self.user2)
        form_data = self.event7_data_ok
        response = self.client.post(self.event_create_view_url, data=form_data)
        event7 = Event.objects.get(title='Event 7')
        self.assertEqual(event7.content, 'Lorem ipsum event7')
        self.assertEqual(event7.author, self.user2)
        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), EVENT_CREATION_SUCCESS)
        # test redirection
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], f'/event/{event7.uuid}/')

    def test_event_create_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('event-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Créer un évènement')

class EventUpdateViewTestCase(BaseTest):

    def test_event_update_view_post_valid_form(self):
        self.client.force_login(self.user2)
        event_update_url = reverse('event-update', args=(self.event4.uuid,))
        form_data = self.event4_data_update
        response = self.client.post(event_update_url, data=form_data)
        event4_up = Event.objects.get(uuid=self.event4.uuid)
        # Test event after update
        self.assertEqual(event4_up.title, 'Event 4 update')
        self.assertEqual(event4_up.updated_event.first().updater, self.user2)
        self.assertEqual(event4_up.updated_event.first().update_reason, 'Event 4 update reason')
        # Test message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), EVENT_UPDATE_SUCCESS)

    def test_event_update_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('event-update', args=(self.event4.uuid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Modifier l\'évènement')

class EventDeleteViewTestCase(BaseTest):

    def test_new_event_delete_view_post_valid_form(self):
        self.client.force_login(self.user2)
        event_delete_url = reverse('event-delete', args=(self.event6.uuid,))
        form_data = self.event6_delete
        response = self.client.post(event_delete_url, data=form_data)
        event6_del = Event.objects.get(uuid=self.event6.uuid)
        # Test new event after delete
        self.assertEqual(event6_del.status, 'DELETED')
        self.assertEqual(event6_del.deleted_event.first().deleter, self.user2)
        self.assertEqual(event6_del.deleted_event.first().deletion_reason, 'Event 6 delete reason')
        # Test message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), EVENT_DELETE_SUCCESS)

    def test_old_event_delete_view_post_valid_form(self):
        self.client.force_login(self.user1)
        event_delete_url = reverse('event-delete', args=(self.event3.uuid,))
        form_data = self.event3_delete
        response = self.client.post(event_delete_url, data=form_data)
        event3_del = Event.objects.get(uuid=self.event3.uuid)
        # Test old event after delete
        self.assertEqual(event3_del.status, 'DELETED')
        self.assertEqual(event3_del.deleted_event.first().deleter, self.user1)
        self.assertEqual(event3_del.deleted_event.first().deletion_reason, 'Event 3 delete reason')
        # Test message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), EVENT_DELETE_SUCCESS)

    def test_new_event_delete_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('event-delete', args=(self.event6.uuid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Supprimer l\'évènement')

    def test_old_event_delete_view_get(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('event-delete', args=(self.event3.uuid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Supprimer l\'évènement')
