#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='news/', view=views.NewsListView.as_view(), name='news-list'),
    path(route='news/<uuid:uuid>/', view=views.NewsDetailView.as_view(), name='news-detail'),
    path(route='news/create/', view=views.NewsCreateView.as_view(), name='news-create'),
    path(route='news/<uuid:uuid>/update', view=views.NewsUpdateView.as_view(), name='news-update'),
    path(route='news/<uuid:uuid>/delete', view=views.NewsDeleteView.as_view(), name='news-delete'),
    path(route='faq/', view=views.FaqCategoryView.as_view(), name='faq-list'),
    path(route='faq/<str:category>', view=views.FaqListView.as_view(), name='faq-list'),
    path(route='faq/<uuid:uuid>/', view=views.FaqDetailView.as_view(), name='faq-detail'),
    path(route='events/', view=views.EventListNewView.as_view(), name='event-list-new'),
    path(route='events/ended', view=views.EventListOldView.as_view(), name='event-list-old'),
    path(route='events/<uuid:uuid>/', view=views.EventDetailView.as_view(), name='event-detail'),
]
