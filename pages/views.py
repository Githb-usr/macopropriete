#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'pages/index.html'

class IntentionsView(TemplateView):
    template_name = 'pages/intentions.html'

class LegalNoticesView(TemplateView):
    template_name = 'pages/legal_notices.html'
