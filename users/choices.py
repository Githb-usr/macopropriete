#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

PENDING = 'PENDING'
VALIDATED = 'VALIDATED'
USER_STATUS = [
    (PENDING, 'En attente'),
    (VALIDATED, 'Validé'),
]
