#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase

from zones.models import Zone
from incidents.models import Incident, IncidentDelete, IncidentTracking

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        self.user1 = User.objects.create_user(
            email='nicolas.martin@free.fr',
            first_name='Nicolas',
            last_name='Martin',
            )

        self.zone1 = Zone.objects.create(
            code='Z1',
            name='Zone 1',
            description='Lorem ipsum zone',
            )

        self.incident1 = Incident.objects.create(
            category='DAMAGE',
            content='Lorem ipsum',
            author=self.user1,
            zone=self.zone1,
            )

        self.incident_delete1 = IncidentDelete.objects.create(
            incident=self.incident1,
            deleter=self.user1,
            deletion_reason='Lorem ipsum delete',
            )

        self.incident_tracking1 = IncidentTracking.objects.create(
            incident=self.incident1,
            status='PENDING',
            )

        return super().setUp()
    
class IncidentModelTestCase(BaseTest):

    def test_object_name(self):
        incident = Incident.objects.get(id=self.incident1.pk)
        expected_object_name = f'Incident - {incident.category}'
        self.assertEquals(expected_object_name, str(incident))

    def test_display_author(self):
        incident = Incident.objects.get(id=self.incident1.pk)
        expected_author_name = incident.display_author()
        self.assertEquals(expected_author_name, 'Nicolas Martin')

class IncidentDeleteModelTestCase(BaseTest):

    def test_display_deleter(self):
        incident_delete = IncidentDelete.objects.get(id=self.incident_delete1.pk)
        expected_deleter_name = incident_delete.display_deleter()
        self.assertEquals(expected_deleter_name, 'Nicolas Martin')

class IncidentTrackingModelTestCase(BaseTest):
    
    def test_object_name(self):
        incident_tracking = IncidentTracking.objects.get(id=self.incident_tracking1.pk)
        expected_object_name = incident_tracking.status
        self.assertEquals(expected_object_name, str(incident_tracking))
