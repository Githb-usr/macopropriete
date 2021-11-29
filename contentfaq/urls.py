#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(
        route='faq/',
        view=views.FaqCategoryListView.as_view(),
        name='faq-cat-list',
    ),
    path(
        route='faq/<str:category>',
        view=views.FaqCategoryView.as_view(),
        name='faq-category',
    ),
    path(
        route='faq/create/',
        view=views.faq_create_view,
        name='faq-create',
    ),
    path(
        route='faq/<uuid:uuid>/update',
        view=views.faq_update_view,
        name='faq-update',
    ),
    path(
        route='faq/<uuid:uuid>/delete',
        view=views.faq_delete_view,
        name='faq-delete',
    ),
]
