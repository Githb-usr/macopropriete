#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.utils.html import strip_tags

"""
    Settings file
    To manage users application constants
"""

ACCOUNT_VALIDATION_SUBJECT = "Création de votre compte utilisateur sur le site de la copropriété du Parc de la Chana"
ACCOUNT_VALIDATION_HTML_MESSAGE = render_to_string('users/account_validation_mail.html', {'context': 'values'})
ACCOUNT_VALIDATION_PLAIN_MESSAGE = strip_tags(ACCOUNT_VALIDATION_HTML_MESSAGE)
REGISTRATION_ALERT_SUCCESS_MSG = "Votre compte a bien été créé, vous pouvez désormais vous connecter."
LOGIN_ALERT_SUCCESS_MSG = "Connexion à votre compte réussie !"
LOGOUT_MSG = "Vous avez bien été déconnecté(e) !"
