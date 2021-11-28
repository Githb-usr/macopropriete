#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Messages
##########
EVENT_CREATION_SUCCESS = 'L\'évènement a bien été créé !'
EVENT_DELETE_SUCCESS = 'L\'évènement a bien été supprimé !'
EVENT_UPDATE_SUCCESS = 'L\'évènement a bien été mis à jour !'

# Categories
############
CONDOMINIUM = 'CONDOMINIUM'
MEETING = 'MEETING'
MISCELLANEOUS = 'MISCELLANEOUS'
PARTY = 'PARTY'
WEBSITE = 'WEBSITE'
WORKS = 'WORKS'

EVENT_CATEGORY = [
    (CONDOMINIUM, 'Copropriété'),
    (WEBSITE, 'Le site'),
    (MEETING, 'Réunion'),
    (PARTY, 'Fête'),
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
