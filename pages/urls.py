#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.show_index, name='homepage'),
    path('legal_notices/', TemplateView.as_view(template_name='pages/legal_notices.html'), name='legal-notices'),
]
