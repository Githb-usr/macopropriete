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
ACCOUNT_VALIDATION_URL = 'account/validation'
ALREADY_VALIDATED_ACCOUNT_MSG = "Votre compte utilisateur était déjà validé.\n\n Vous pouvez vous connecter."
VALIDATED_ACCOUNT_SUCCESS_MSG = "Votre compte utilisateur a bien été validé.\n\n Vous pouvez désormais vous connecter."
ACCOUNT_DOES_NOT_EXIST = "Ce compte utilisateur n'existe pas !"
LOGIN_ALERT_SUCCESS_MSG = "Connexion à votre compte réussie !"
LOGOUT_MSG = "Vous avez bien été déconnecté(e) !"
