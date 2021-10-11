#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='news/', view=views.NewsListView.as_view(), name='article-list'),
    path(route='news/<int:pk>/', view=views.NewsDetailView.as_view(), name='article-detail'),
]
