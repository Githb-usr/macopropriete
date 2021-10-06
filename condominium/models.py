#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.urls import reverse

class Lot(models.Model):
    """
    Model of the "condominium_lot" table in the database
    """
    # lot type
    APARTMENT = 'Apartment'
    CELLAR = 'Cellar'
    INDIVIDUAL_GARAGE = 'Individual garage'
    LOT_TYPE = [
        (APARTMENT, 'Appartement'),
        (CELLAR, 'Cave'),
        (INDIVIDUAL_GARAGE, 'Garage'),
    ]
    lot_type = models.CharField(max_length=20, choices=LOT_TYPE)
    number = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    share = models.CharField(max_length=15)
    image = models.ImageField(upload_to='condominium/lot/')
    condominium = models.ForeignKey(Condominium, on_delete=models.CASCADE, related_name='lot_condominium')

    def __str__(self):
        return f'{self.lot_type} - {self.number}'
    
    class Meta:
        verbose_name_plural = "lots"

class Ownership(models.Model):
    """
    Intermediate model between "Lot" and "Person", defined to add fields
    """
    owner = models.ForeignKey('users.Person', on_delete=models.CASCADE, related_name='lot_owner')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='owned_lot')
    acquisition_date = models.DateTimeField(null=True, blank=True)

class Condominium(models.Model):
    """
    Model of the "condominium_condominium" table in the database
    """
    # type of condominium
    BUILDING = 'Building'
    INDIVIDUAL_GARAGES = 'Individual garages'
    PARK = 'Park'
    CONDOMINIUM_TYPE = [
        (BUILDING, 'Immeuble'),
        (INDIVIDUAL_GARAGES, 'Garages'),
        (PARK, 'Parc'),
    ]
    condominium_type = models.CharField(max_length=30, choices=CONDOMINIUM_TYPE)
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    share = models.CharField(max_length=15)
    image = models.ImageField(upload_to='condominium/condominium/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "condominiums"

class Zone(models.Model):
    """
    Model of the "condominium_zone" table in the database
    """
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='condominium/zone/')

    def __str__(self):
        return f'{self.name} ({self.code})'
    
    class Meta:
        verbose_name_plural = "zones"
