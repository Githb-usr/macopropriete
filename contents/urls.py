#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='news/', view=views.NewsListView.as_view(), name='news-list'),
    path(route='news/<int:pk>/', view=views.NewsDetailView.as_view(), name='news-detail'),
    path(route='faq/', view=views.FaqListView.as_view(), name='faq-list'),
    path(route='faq/<int:pk>/', view=views.FaqDetailView.as_view(), name='faq-detail'),
]
