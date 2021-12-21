#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase

from zones.models import Zone
from comments.models import Comment, CommentDelete
from contentevent.models import Event
from contentnews.models import News
from incidents.models import Incident

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.zone1 = Zone.objects.create(
            code='Z1',
            name='Zone 1',
            description='Lorem ipsum zone',
        )

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

        self.news1 = News.objects.create(
            category='MEETING',
            title='Titre news 1',
            content='Lorem ipsum news',
            status='ACTIVATED',
            author=self.user1,
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

        self.incident1 = Incident.objects.create(
            category='DAMAGE',
            content='Lorem ipsum',
            author=self.user1,
            zone=self.zone1,
        )

        self.comment1 = Comment.objects.create(
            content='Lorem ipsum comment',
            status='ACTIVATED',
            author=self.user1,
            news=self.news1,
        )

        self.comment_delete1 = CommentDelete.objects.create(
            comment=self.comment1,
            deleter=self.user2,
            deletion_reason='Lorem ipsum comment delete',
        )

        return super().setUp()

class CommentModelTestCase(BaseTest):

    def test_object_name(self):
        comment = Comment.objects.get(id=self.comment1.pk)
        expected_object_name = 'Commentaire de {}'.format(comment.author)
        self.assertEquals(expected_object_name, str(comment))

    def test_display_author(self):
        comment = Comment.objects.get(id=self.comment1.pk)
        expected_author_name = comment.display_author()
        self.assertEquals(expected_author_name, 'Nicolas Martin')

class CommentDeleteModelTestCase(BaseTest):

    def test_display_deleter(self):
        comment_delete = CommentDelete.objects.get(id=self.comment_delete1.pk)
        expected_deleter_name = comment_delete.display_deleter()
        self.assertEquals(expected_deleter_name, 'Valérie Plouf')
