#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from config.settings.base import EMAIL_HOST_USER

def choice_translation(choice_list, original_item):
    translated_item = ''
    for item in choice_list:
        if item[0] == original_item:
            translated_item = item[1]

    return translated_item

def generic_send_mail(mail_subject, html_page, recipients, email_context):
    subject = mail_subject
    from_email = EMAIL_HOST_USER
    html_message = render_to_string(html_page, email_context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        from_email,
        [recipients],
        html_message=html_message
    )
