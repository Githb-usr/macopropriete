#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Messages
##########
QUESTION_CREATION_SUCCESS = 'La question a bien été créée !'
QUESTION_DELETE_SUCCESS = 'La question a bien été supprimée !'
QUESTION_UPDATE_SUCCESS = 'La question a bien été mise à jour !'

# Category choices
##################
BUILDINGS = 'BUILDINGS'
CAR_PARKS = 'CAR PARKS'
INDIVIDUAL_GARAGES = 'INDIVIDUAL GARAGES'
MISCELLANEOUS = 'MISCELLANEOUS'
PARK = 'PARK'

FAQ_CATEGORY = [
    (BUILDINGS, 'Les bâtiments'),
    (INDIVIDUAL_GARAGES, 'Les garages'),
    (PARK, 'Le parc'),
    (CAR_PARKS, 'Les parkings'),
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
