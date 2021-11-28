#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='events/', view=views.EventListNewView.as_view(), name='event-list-new'),
    path(route='events/ended', view=views.EventListOldView.as_view(), name='event-list-old'),
    path(route='events/<uuid:uuid>/', view=views.EventDetailView.as_view(), name='event-detail'),
    path(route='events/create/', view=views.event_create_view, name='event-create'),
    path(route='events/<uuid:uuid>/update', view=views.event_update_view, name='event-update'),
    path(route='events/<uuid:uuid>/delete', view=views.event_delete_view, name='event-delete'),
]
