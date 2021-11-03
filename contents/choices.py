#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################
## All categories ##
####################

# Categories for news, events
CONDOMINIUM = 'CONDOMINIUM'
MEETING = 'MEETING'
PARTY = 'PARTY'
WEBSITE = 'WEBSITE'
WORKS = 'WORKS'

# Categories for FAQ
BUILDINGS = 'BUILDINGS'
CAR_PARKS = 'CAR PARKS'
INDIVIDUAL_GARAGES = 'INDIVIDUAL GARAGES'
PARK = 'PARK'

# Categories for news, FAQ, events
MISCELLANEOUS = 'MISCELLANEOUS'

# Categories for incidents
ACCIDENT = 'ACCIDENT'
BREAKDOWN = 'BREAKDOWN'
DAMAGE = 'DAMAGE'
WATER_LEAKAGE = 'WATER_LEAKAGE'

# Status for incident tracking
PENDING = 'PENDING'
REJECTED = 'REJECTED'
REGISTERED = 'REGISTERED'
IN_PROGRESS = 'IN_PROGRESS'
CLOSED = 'CLOSED'

# Status for all contents
ACTIVATED = 'ACTIVATED'
DELETED = 'DELETED'

######################
## All choice lists ##
######################

# News categories
NEWS_CATEGORY = [
    (CONDOMINIUM, 'Copropriété'),
    (MEETING, 'Réunion'),
    (PARTY, 'Fête'),
    (WEBSITE, 'Site'),
    (WORKS, 'Travaux'),
    (MISCELLANEOUS, 'Divers'),
]

# Event categories
EVENT_CATEGORY = [
    (CONDOMINIUM, 'Copropriété'),
    (WEBSITE, 'Le site'),
    (MEETING, 'Réunion'),
    (PARTY, 'Fête'),
    (WORKS, 'Travaux'),
    (MISCELLANEOUS, 'Divers'),
]

# FAQ categories
FAQ_CATEGORY = [
    (BUILDINGS, 'Les bâtiments'),
    (INDIVIDUAL_GARAGES, 'Les garages'),
    (PARK, 'Le parc'),
    (CAR_PARKS, 'Les parkings'),
    (MISCELLANEOUS, 'Divers'),
]

# Incident categories
INCIDENT_CATEGORY = [
    (ACCIDENT, 'Accident'),
    (DAMAGE, 'Dégradation'),
    (WATER_LEAKAGE, 'Fuite d\'eau'),
    (BREAKDOWN, 'Panne'),        
    (MISCELLANEOUS, 'Divers'),
]

# Incident tracking status
TRACKING_STATUS = [
    (PENDING, 'en attente'),
    (REJECTED, 'rejeté'),
    (REGISTERED, 'enregistré'),
    (IN_PROGRESS, 'en cours'),
    (CLOSED, 'fermé'),
]

# Status of different types of content
CONTENT_STATUS = [
    (ACTIVATED, 'Actif'),
    (DELETED, 'Supprimé'),
]