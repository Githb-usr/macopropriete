#!/usr/bin/env python
# -*- coding: utf-8 -*-

CONDOMINIUM = 'CONDOMINIUM'
MEETING = 'MEETING'
MISCELLANEOUS = 'MISCELLANEOUS'
PARTY = 'PARTY'
WEBSITE = 'WEBSITE'
WORKS = 'WORKS'
SUBJECTS = [
    ('','---------'),
    (CONDOMINIUM, 'La copropriété'),
    (WEBSITE, 'Le site'),
    (MEETING, 'Les réunions'),
    (PARTY, 'Les fêtes'),
    (WORKS, 'Les travaux'),
    (MISCELLANEOUS, 'Autre'),
]

OWNER_OCCUPIER = 'OWNER OCCUPIER'
OWNER_LESSOR = 'OWNER LESSOR'
TENANT = 'TENANT'
SYNDIC = 'SYNDIC'
USER_TYPE = [
    ('','---------'),
    (OWNER_OCCUPIER, 'Copropriétaire occupant'),
    (OWNER_LESSOR, 'Copropriétaire bailleur'),
    (TENANT, 'Locataire'),
    (SYNDIC, 'Membre du Syndic'),
]
