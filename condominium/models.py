#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import uuid

from condominium.settings import CONDOMINIUM_TYPE, INDIVIDUAL_GARAGE_LOCATION, LOT_TYPE
from config.settings.base import AUTH_USER_MODEL

class Zone(models.Model):
    """
    Model of the "condominium_zone" table in the database
    """
    code = models.CharField(
        max_length=10,
        verbose_name='Code',
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Nom',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='condominium/zone/',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        verbose_name='UUID',
    )

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        verbose_name_plural = "zones"

class Condominium(models.Model):
    """
    Model of the "condominium_condominium" table in the database
    """
    condominium_type = models.CharField(
        max_length=30,
        choices=CONDOMINIUM_TYPE,
        verbose_name='Type',
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Nom',
    )
    number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Numéro',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    share = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        verbose_name='Quote-part',
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='condominium/condominium/',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        verbose_name='UUID',
    )

    def __str__(self):
        return f'Copropriété {self.name}'

    class Meta:
        verbose_name_plural = "condominiums"

class IndividualGarages(models.Model):
    condominium = models.OneToOneField(
        Condominium,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    rows_number = models.IntegerField(
        verbose_name='Nombre de rangées',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    garages_number = models.IntegerField(
        verbose_name='Nombre de garages',
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='condominium/condominium/',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        verbose_name='UUID',
    )

    def __str__(self):
        return 'Garages'

class Building(models.Model):
    condominium = models.OneToOneField(
        Condominium,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Nom',
    )
    letter = models.CharField(
        max_length=1,
        verbose_name='Lettre',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    entrances_number = models.IntegerField(
        verbose_name='Nombre d\'entrées',
    )
    bike_room = models.BooleanField(
        default=False,
        verbose_name='Garage à vélos',
    )

    def __str__(self):
        return f'Bâtiment {self.name}'

    class Meta:
        verbose_name_plural = "buildings"

class Entrance(models.Model):
    number = models.CharField(
        max_length=3,
        verbose_name='Numéro',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    floors_number = models.IntegerField(
        verbose_name='Nombre de niveaux',
    )
    apartments_number = models.IntegerField(
        verbose_name='Nombre d\'appartements',
    )
    cellars_number = models.IntegerField(
        verbose_name='Nombre de caves',
    )
    elevator = models.BooleanField(
        default=False,
        verbose_name='Ascenseur',
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='condominium/condominium/',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        verbose_name='UUID',
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='building_of_entrance',
    )

    def __str__(self):
        return f'Entrée {self.building.letter}{self.number}'

    class Meta:
        verbose_name_plural = "entrances"

class Lot(models.Model):
    """
    Model of the "condominium_lot" table in the database
    """
    lot_type = models.CharField(
        max_length=20,
        choices=LOT_TYPE,
        verbose_name='Type',
    )
    number = models.CharField(
        max_length=10,
        verbose_name='Numéro',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    share = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        verbose_name='Quote-part',
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='condominium/lot/',
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        verbose_name='UUID',
    )
    condominium = models.ForeignKey(
        Condominium,
        on_delete=models.CASCADE,
        related_name='lot_condominium',
    )

    def __str__(self):
        return f'Lot {self.number} ({self.lot_type})'

    class Meta:
        verbose_name_plural = "lots"

class Apartment(models.Model):
    lot = models.OneToOneField(
        Lot,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    number = models.CharField(
        max_length=10,
        verbose_name='Numéro',
    )
    door = models.CharField(
        max_length=10,
        verbose_name='Porte',
    )
    floor = models.IntegerField(
        verbose_name='Etage',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    parking_space_number = models.IntegerField(
        verbose_name='Place de parking',
    )
    balcony = models.BooleanField(
        default=True,
        verbose_name='Balcon',
    )
    garden = models.BooleanField(
        default=False,
        verbose_name='Jardin',
    )
    entrance = models.ForeignKey(
        Entrance,
        on_delete=models.CASCADE,
        related_name='entrance_apartment',
    )
    parking_space_zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name='parking_space_zone',
    )

    def __str__(self):
        return f'Appartement {self.number}'

    class Meta:
        verbose_name_plural = "apartments"

class Cellar(models.Model):
    lot = models.OneToOneField(
        Lot,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    number = models.CharField(
        max_length=10,
        verbose_name='Numéro',
    )
    floor = models.IntegerField(
        verbose_name='Etage',
    )
    entrance = models.ForeignKey(
        Entrance,
        on_delete=models.CASCADE,
        related_name='entrance_cellar',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )

    def __str__(self):
        return f'Cave {self.number}'

    class Meta:
        verbose_name_plural = "cellars"

class IndividualGarage(models.Model):
    lot = models.OneToOneField(
        Lot,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    number = models.CharField(
        max_length=10,
        verbose_name='Numéro',
    )
    location = models.CharField(
        max_length=20,
        choices=INDIVIDUAL_GARAGE_LOCATION,
        verbose_name='Emplacement',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )

    def __str__(self):
        return f'Garage {self.number}'

    class Meta:
        verbose_name_plural = "individual garages"

class Ownership(models.Model):
    """
    Intermediate model between "Lot" and "User", defined to add fields
    """
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lot_owner',
    )
    lot = models.ForeignKey(
        Lot,
        on_delete=models.CASCADE,
        related_name='owned_lot',
    )
    acquisition_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Acquisition le',
    )
