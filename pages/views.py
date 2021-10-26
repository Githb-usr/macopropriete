#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from pages.forms import ContactForm

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

class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = 'contact/success'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'pages/contact_success.html'
