#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template.loader import render_to_string
from django.utils.html import strip_tags

"""
Settings file
To manage users application constants
"""

# For account validation email
##############################
ACCOUNT_VALIDATION_SUBJECT = "Création de votre compte utilisateur sur le site de la copropriété du Parc de la Chana"
ACCOUNT_VALIDATION_HTML_MESSAGE = render_to_string('users/account_validation_mail.html', {'context': 'values'})
ACCOUNT_VALIDATION_PLAIN_MESSAGE = strip_tags(ACCOUNT_VALIDATION_HTML_MESSAGE)
ACCOUNT_VALIDATION_URL = 'account/validation'

# Messages
##########
ALREADY_VALIDATED_ACCOUNT_MSG = "Votre compte utilisateur était déjà validé.\n\n Vous pouvez vous connecter."
VALIDATED_ACCOUNT_SUCCESS_MSG = "Votre compte utilisateur a bien été validé.\n\n Vous pouvez désormais vous connecter."
ACCOUNT_DOES_NOT_EXIST = "Ce compte utilisateur n'existe pas !"
LOGIN_ALERT_SUCCESS_MSG = "Connexion à votre compte réussie !"
LOGOUT_MSG = "Vous avez bien été déconnecté(e) !"

# User type choices
###################
OWNER_OCCUPIER = 'OWNER OCCUPIER'
OWNER_LESSOR = 'OWNER LESSOR'
TENANT = 'TENANT'
SYNDIC = 'SYNDIC'
USER_TYPE = [
    (OWNER_OCCUPIER, 'Copropriétaire occupant'),
    (OWNER_LESSOR, 'Copropriétaire bailleur'),
    (TENANT, 'Locataire'),
    (SYNDIC, 'Syndic'),
]

# User status choices
#####################
PENDING = 'PENDING'
VALIDATED = 'VALIDATED'
USER_STATUS = [
    (PENDING, 'En attente'),
    (VALIDATED, 'Validé'),
]

# User address choices
######################
A1 = 'A1'
A2 = 'A2'
A3 = 'A3'
B1 = 'B1'
B2 = 'B2'
B3 = 'B3'
C1 = 'C1'
C2 = 'C2'
C3 = 'C3'
USER_ADDRESS = [
    (A1, 'Tulipier 1'),
    (A2, 'Tulipier 2'),
    (A3, 'Tulipier 3'),
    (B1, 'Magnolia 1'),
    (B2, 'Magnolia 2'),
    (B3, 'Magnolia 3'),
    (C1, 'Sophora 1'),
    (C2, 'Sophora 2'),
    (C3, 'Sophora 3'),
]
