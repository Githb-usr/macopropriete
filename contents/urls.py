#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='news/', view=views.NewsListView.as_view(), name='news-list'),
    path(route='news/<uuid:uuid>/', view=views.NewsDetailView.as_view(), name='news-detail'),
    path(route='faq/', view=views.FaqListView.as_view(), name='faq-list'),
    path(route='faq/<uuid:uuid>/', view=views.FaqDetailView.as_view(), name='faq-detail'),
    path(route='evenements/', view=views.EventListView.as_view(), name='event-list'),
    path(route='evenements/<uuid:uuid>/', view=views.EventDetailView.as_view(), name='event-detail'),
]
