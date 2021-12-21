#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Inident categories
####################
ACCIDENT = 'ACCIDENT'
BREAKDOWN = 'BREAKDOWN'
DAMAGE = 'DAMAGE'
MISCELLANEOUS = 'MISCELLANEOUS'
WATER_LEAKAGE = 'WATER_LEAKAGE'

INCIDENT_CATEGORY = [
    (ACCIDENT, 'Accident'),
    (DAMAGE, 'Dégradation'),
    (WATER_LEAKAGE, 'Fuite d\'eau'),
    (BREAKDOWN, 'Panne'),
    (MISCELLANEOUS, 'Divers'),
]

# Incident tracking status
##########################
PENDING = 'PENDING'
REJECTED = 'REJECTED'
REGISTERED = 'REGISTERED'
IN_PROGRESS = 'IN_PROGRESS'
CLOSED = 'CLOSED'

TRACKING_STATUS = [
    (PENDING, 'en attente'),
    (REJECTED, 'rejeté'),
    (REGISTERED, 'enregistré'),
    (IN_PROGRESS, 'en cours'),
    (CLOSED, 'fermé'),
]
