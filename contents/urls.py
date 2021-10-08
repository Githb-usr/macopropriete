#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='news/', view=views.ArticleListView.as_view(template_name='contents/article_list.html'), name='article-list'),
    path(route='news/<int:pk>/', view=views.ArticleDetailView.as_view(), name='article-detail'),
]
