#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='news/', view=views.NewsListView.as_view(), name='news-list'),
    path(route='news/create/', view=views.news_create_view, name='news-create'),
    path(route='news/<uuid:uuid>/', view=views.NewsDetailView.as_view(), name='news-detail'),
    path(route='news/<uuid:uuid>/update', view=views.news_update_view, name='news-update'),
    path(route='news/<uuid:uuid>/delete', view=views.NewsDeleteView.as_view(), name='news-delete'),
    path(route='faq/', view=views.FaqCategoryListView.as_view(), name='faq-cat-list'),
    path(route='faq/<str:category>', view=views.FaqCategoryView.as_view(), name='faq-category'),
    path(route='faq/create/', view=views.faq_create_view, name='faq-create'),
    path(route='faq/<uuid:uuid>/update', view=views.faq_update_view, name='faq-update'),
    path(route='events/', view=views.EventListNewView.as_view(), name='event-list-new'),
    path(route='events/ended', view=views.EventListOldView.as_view(), name='event-list-old'),
    path(route='events/<uuid:uuid>/', view=views.EventDetailView.as_view(), name='event-detail'),
    path(route='events/create/', view=views.event_create_view, name='event-create'),
]
