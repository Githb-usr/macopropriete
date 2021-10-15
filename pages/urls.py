#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(route='', view=views.IndexView.as_view(), name='homepage'),
    path(route='intentions/', view=views.IntentionsView.as_view(), name='intentions'),
    path(route='legal_notices/', view=views.LegalNoticesView.as_view(), name='legal-notices'),
]
