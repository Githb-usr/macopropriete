#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Managing the creation of a user
        """
        if not email:
            raise ValueError('Vous devez entrer un email valide')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password=None, is_staff=True, is_superuser=True):
        """
        Managing the creation of a superuser
        """
        if not email:
            raise ValueError('Vous devez entrer un email valide')

        superuser = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        superuser.set_password(password)
        superuser.save(using=self._db)

        return superuser

class User(AbstractUser):
    """
    Model of the "users_user" table in the database
    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Adresse email',
        )
    username = models.CharField(max_length=30, blank=True, null=True, unique=True, verbose_name='Pseudonyme')
    is_active = models.BooleanField(default=True, verbose_name='Utilisateur actif')
    is_staff = models.BooleanField(default=False, verbose_name='Administrateur')
    is_superuser = models.BooleanField(default=False, verbose_name='Super administrateur')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Inscription')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Dernière connexion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    OWNER_OCCUPIER = 'Owner occupier'
    OWNER_LESSOR = 'Owner lessor'
    TENANT = 'Tenant'
    SYNDIC = 'Syndic'
    USER_TYPE = [
        (OWNER_OCCUPIER, 'Copropriétaire occupant'),
        (OWNER_LESSOR, 'Copropriétaire bailleur'),
        (TENANT, 'Locataire'),
        (SYNDIC, 'Syndic'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default='OWNER_OCCUPIER', verbose_name='Catégorie d\'utilisateur')
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Prénom')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nom')
    contact_email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='Adresse email de contact')
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Téléphone')
    avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='Avatar')
    about = models.TextField(null=True, blank=True, verbose_name='A propos de moi')
    is_resident = models.BooleanField(default=True, verbose_name='Résident')
    is_union_council = models.BooleanField(default=False, verbose_name='Membre du Conseil Syndical')
    PENDING = 'Pending'
    VALIDATED = 'Validated'
    USER_STATUS = [
        (PENDING, 'En attente'),
        (VALIDATED, 'Validé'),
    ]
    status = models.CharField(max_length=15, choices=USER_STATUS, default=PENDING, verbose_name='Statut')

    objects = UserManager()

    # Main Field for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'

        return self.email.split('@')[0]

    class Meta:
        ordering = ('-date_joined', '-updated_at', )
