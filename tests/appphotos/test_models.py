#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase

from photos.models import Photo

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        self.user = User.objects.create_user(
            email='nicolas.martin@free.fr',
            first_name='Nicolas',
            last_name='Martin',
            password='fhh456GG455t'
            )

        self.photo = Photo.objects.create(
            image='nicole.jpg',
            caption='Photo de Nicole',
            uploader=self.user
            )

        return super().setUp()
    
class PhotoModelTestCase(BaseTest):

    def test_object_name_is_caption(self):
        photo = Photo.objects.get(id=self.photo.pk)
        expected_object_name = photo.caption
        self.assertEquals(expected_object_name, str(photo))
