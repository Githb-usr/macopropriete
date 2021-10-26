#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

CONDOMINIUM = 'CONDOMINIUM'
MEETING = 'MEETING'
MISCELLANEOUS = 'MISCELLANEOUS'
PARTY = 'PARTY'
WEBSITE = 'WEBSITE'
WORKS = 'WORKS'
SUBJECTS = [
    (CONDOMINIUM, 'Copropriété'),
    (WEBSITE, 'Le site'),
    (MEETING, 'Réunion'),
    (PARTY, 'Fête'),
    (WORKS, 'Travaux'),
    (MISCELLANEOUS, 'Autre'),
]

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50, label='Prénom')
    last_name = forms.CharField(max_length = 50, label='Nom')
    email_address = forms.EmailField(max_length = 150, label='Adresse email')
    message_subject = forms.ChoiceField(choices=SUBJECTS, label='Sujet du message')
    message = forms.CharField(widget = forms.Textarea, max_length = 2500, label='Votre message')
