#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(
        route='events/',
        view=views.EventListNewView.as_view(),
        name='event-list-new',
    ),
    path(
        route='events/ended',
        view=views.EventListOldView.as_view(),
        name='event-list-old',
    ),
    path(
        route='event/<uuid:uuid>/',
        view=views.EventDetailView.as_view(),
        name='event-detail',
    ),
    path(
        route='event/create/',
        view=views.event_create_view,
        name='event-create',
    ),
    path(
        route='event/<uuid:uuid>/update',
        view=views.event_update_view,
        name='event-update',
    ),
    path(
        route='event/<uuid:uuid>/delete',
        view=views.event_delete_view,
        name='event-delete',
    ),
]
