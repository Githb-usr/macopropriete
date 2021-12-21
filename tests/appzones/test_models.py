#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from zones.models import Zone

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.zone1 = Zone.objects.create(
            code='Z1',
            name='Zone 1',
            description='Lorem ipsum zone',
        )

        return super().setUp()

class ZoneModelTestCase(BaseTest):

    def test_object_name(self):
        zone = Zone.objects.get(id=self.zone1.pk)
        expected_object_name = f'{zone.name} ({zone.code})'
        self.assertEquals(expected_object_name, str(zone))
