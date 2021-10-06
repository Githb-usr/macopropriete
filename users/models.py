#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Managing the creation of a user from the registration form
        """
        if not email:
            raise ValueError('Vous devez entrer un email valide')

        user = self.model(
            username=self.model.normalize_username(username),
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractUser):
    """
    Model of the "users_user" table in the database
    """
    username = models.CharField(max_length=30, unique=True, verbose_name='Pseudonyme')
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Adresse email',
        )
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
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Prénom')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nom')
    contact_email = models.EmailField(max_length=255, verbose_name='Adresse email de contact')
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Téléphone')
    avatar = models.ImageField(upload_to='users/avatars/')
    about = models.TextField(null=True, blank=True)
    date_joinded = models.DateTimeField(auto_now=True, verbose_name='Inscription')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Dernière connexion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    is_resident = models.BooleanField(default=True)
    is_union_council = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    # Main Field for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'

        return self.email.split('@')[0]

    class Meta:
        ordering = ('-date_joined', '-updated_at', )
