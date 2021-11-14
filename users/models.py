#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid

from condominium.models import Lot
from contents.models import Comment, Event, Faq, Incident, News
from users.choices import OWNER_OCCUPIER, PENDING, USER_ADDRESS, USER_STATUS, USER_TYPE

class UserManager(BaseUserManager):
    """
    Define a model manager for User model with no username field.
    """

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a new user with email but no password required by default
        """
        if not email:
            raise ValueError('Vous devez entrer un email valide')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser
        """
        if not email:
            raise ValueError('Vous devez entrer un email valide')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Un super utilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Un super utilisateur doit avoir is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """
    Model of the "users_user" table in the database
    """
    username = None
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Prénom'
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Nom'
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Adresse email',
    )
    address = models.CharField(
        max_length=25,
        choices=USER_ADDRESS,
        blank=True,
        null=True,
        verbose_name='Bâtiment'
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE,
        default=OWNER_OCCUPIER,
        verbose_name='Catégorie d\'utilisateur'
    )
    status = models.CharField(
        max_length=15,
        choices=USER_STATUS,
        default=PENDING,
        verbose_name='Statut'
    )
    is_resident = models.BooleanField(default=True, verbose_name='Résident')
    is_union_council = models.BooleanField(default=False, verbose_name='Membre du Conseil Syndical')
    is_active = models.BooleanField(default=True, verbose_name='Utilisateur actif')
    is_staff = models.BooleanField(default=False, verbose_name='Administrateur')
    is_superuser = models.BooleanField(default=False, verbose_name='Super administrateur')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Dernière connexion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Dernière modification')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Inscription')
    avatar = models.ImageField(
        validators=[FileExtensionValidator(['gif', 'jpeg', 'jpg', 'png'])],
        upload_to='users/',
        null=True,
        blank=True,
        verbose_name='Avatar'
    )
    about = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name='A propos de moi'
    )
    contact_email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Adresse email de contact'
    )
    phone_number_regex = RegexValidator(regex=r"^0\d{9}$")
    phone_number = models.CharField(
        validators=[phone_number_regex],
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Téléphone'
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    faq_to_update = models.ManyToManyField(Faq, through='contents.FaqUpdate', related_name='faq_update')
    faq_to_delete = models.ManyToManyField(Faq, through='contents.FaqDelete', related_name='faq_delete')
    event_to_update = models.ManyToManyField(Event, through='contents.EventUpdate', related_name='event_update')
    event_to_delete = models.ManyToManyField(Event, through='contents.EventDelete', related_name='event_delete')
    incident_to_delete = models.ManyToManyField(Incident, through='contents.IncidentDelete', related_name='incident_delete')
    comment_to_delete = models.ManyToManyField(Comment, through='contents.CommentDelete', related_name='comment_delete')
    lot_owned = models.ManyToManyField(Lot, through='condominium.Ownership', related_name='lot_owned')

    objects = UserManager()

    # Main field for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'

        return self.email.split('@')[0]

    def get_absolute_url(self):
        return reverse('profile', kwargs={'uuid': self.uuid})

    class Meta:
        ordering = ('-date_joined', '-updated_at', )
