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
