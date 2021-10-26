#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path(route='', view=views.IndexView.as_view(), name='homepage'),
    path(route='contact/', view=views.ContactFormView.as_view(), name='contact'),
    path(route='contact/success', view=views.ContactSuccessView.as_view(), name='contact-success'),
    path(route='intentions', view=views.IntentionsView.as_view(), name='intentions'),
    path(route='legal_notices', view=views.LegalNoticesView.as_view(), name='legal-notices'),
]
