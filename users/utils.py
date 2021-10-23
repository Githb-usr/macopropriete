#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.mail import send_mail
import random
import string

from config.settings import EMAIL_HOST_USER

def get_random_string(length):
    # With combination of lower and upper case
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
    
def generic_send_mail(subject, recipient_adress, html_message):
    send_mail(
            subject=subject,
            message=html_message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[recipient_adress],
            fail_silently=False,
        )