#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ckeditor.widgets import CKEditorWidget
from django import forms

from pages.settings import SUBJECTS, USER_TYPE

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50, label='Prénom')
    last_name = forms.CharField(max_length = 50, label='Nom')
    email_address = forms.EmailField(max_length = 150, label='Adresse email')
    user_type = forms.ChoiceField(choices=USER_TYPE, label='Vous êtes')
    message_subject = forms.ChoiceField(choices=SUBJECTS, label='Sujet du message')
    cc_myself = forms.BooleanField(required=False, label='Recevoir une copie de mon message')
    message = forms.CharField(widget=CKEditorWidget(), max_length = 2500, label='Votre message')
