#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Messages
##########
NEWS_CREATION_SUCCESS = 'La news a bien été créée !'
NEWS_DELETE_SUCCESS = 'La news a bien été supprimée !'
NEWS_UPDATE_SUCCESS = 'La news a bien été mise à jour !'

# Categories
############
CONDOMINIUM = 'CONDOMINIUM'
MEETING = 'MEETING'
MISCELLANEOUS = 'MISCELLANEOUS'
PARTY = 'PARTY'
WEBSITE = 'WEBSITE'
WORKS = 'WORKS'

NEWS_CATEGORY = [
    (CONDOMINIUM, 'Copropriété'),
    (MEETING, 'Réunion'),
    (PARTY, 'Fête'),
    (WEBSITE, 'Site'),
    (WORKS, 'Travaux'),
    (MISCELLANEOUS, 'Divers'),
]

# Status
########
ACTIVATED = 'ACTIVATED'
DELETED = 'DELETED'

STATUS = [
    (ACTIVATED, 'Actif'),
    (DELETED, 'Supprimé'),
]
