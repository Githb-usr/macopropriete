#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_uuid'] = self.request.user.uuid
        return context

class IntentionsView(TemplateView):
    template_name = 'pages/intentions.html'

class LegalNoticesView(TemplateView):
    template_name = 'pages/legal_notices.html'
