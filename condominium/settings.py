#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Type of condominium
BUILDING = 'Building'
INDIVIDUAL_GARAGES = 'Individual garages'
PARK = 'Park'
CONDOMINIUM_TYPE = [
    (BUILDING, 'Immeuble'),
    (INDIVIDUAL_GARAGES, 'Garages'),
    (PARK, 'Parc'),
]

# Type of lot
APARTMENT = 'Apartment'
CELLAR = 'Cellar'
INDIVIDUAL_GARAGE = 'Individual garage'
LOT_TYPE = [
    (APARTMENT, 'Appartement'),
    (CELLAR, 'Cave'),
    (INDIVIDUAL_GARAGE, 'Garage'),
]

# Individual garage location
ROW_1 = 'ROW_1'
ROW_2 = 'ROW_2'
INDIVIDUAL_GARAGE_LOCATION = [
    (ROW_1, 'Rangée 1'),
    (ROW_2, 'Rangée 2'),
]
