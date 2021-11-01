#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from config.settings import EMAIL_HOST_USER, ADMIN_RECIPIENTS
from pages.choices import SUBJECTS, USER_TYPE
from pages.forms import ContactForm
from pages.utils import choice_translation, generic_send_mail

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
    success_url = 'success'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        valid_data = form.cleaned_data
        user_type = choice_translation(USER_TYPE, valid_data['user_type'])
        raw_message_subject = choice_translation(SUBJECTS, valid_data['message_subject'])
        admin_message_subject = 'Parc de La Chana : nouveau message sur le thème "{0}"'.format(raw_message_subject)
        user_message_subject = 'Votre message envoyé au Parc de La Chana sur le thème "{0}"'.format(raw_message_subject)
        email_context = {
                'date': timezone.now(),
                'first_name': valid_data['first_name'],
                'last_name': valid_data['last_name'],
                'email_address': valid_data['email_address'],
                'user_type': user_type,
                'message_subject': raw_message_subject,
                'message' : valid_data['message'],
            }

        recipients = ADMIN_RECIPIENTS
        print('TOTOOOOO', recipients)
        html_page = 'pages/contact_to_admin_mail.html'
        generic_send_mail(admin_message_subject, html_page, recipients, email_context)
        if valid_data['cc_myself']:
            recipients = valid_data['email_address']
            print('POUUUUF', recipients)
            html_page = 'pages/contact_copy_to_user_mail.html'
            generic_send_mail(user_message_subject, html_page, recipients, email_context)

        return super(ContactFormView, self).form_valid(form)        

class ContactSuccessView(TemplateView):
    template_name = 'pages/contact_success.html'
