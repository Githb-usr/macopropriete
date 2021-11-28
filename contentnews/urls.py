#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='news/', view=views.NewsListView.as_view(), name='news-list'),
    path(route='news/create/', view=views.news_create_view, name='news-create'),
    path(route='news/<uuid:uuid>/', view=views.NewsDetailView.as_view(), name='news-detail'),
    path(route='news/<uuid:uuid>/update', view=views.news_update_view, name='news-update'),
    path(route='news/<uuid:uuid>/delete', view=views.news_delete_view, name='news-delete'),
]
