#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.core import mail
from django.utils import timezone

from pages.utils import generic_send_mail
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User
from users.settings import ACCOUNT_VALIDATION_SUBJECT, ACCOUNT_VALIDATION_URL
from users.utils import get_random_string

class UserAdmin(admin.ModelAdmin):
    """
    Display of User in the back office
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    empty_value_display = '-empty-'
    list_display = ('email', 'password', 'status', 'is_active', 'is_staff',
                    'date_joined', 'last_login', 'updated_at', 'user_type',
                    'first_name', 'last_name', 'contact_email', 'phone_number',
                    'avatar', 'about', 'is_resident', 'is_union_council', 'address',)
    fieldsets = (
        ('Compte', {'fields': ('email', 'password', 'status', 'uuid')}),
        ('Personne', {'fields': ('user_type', 'first_name', 'last_name', 'address', 'contact_email', 'phone_number',
                    'avatar', 'about',)}),
        ('Statuts', {'fields': ('is_active', 'is_resident', 'is_union_council', 'is_staff',)}),
    )
    list_editable = ('user_type', 'first_name', 'last_name', 'contact_email', 'phone_number', 
                     'is_resident', 'is_union_council',)
    list_filter = ('date_joined', 'is_active','is_resident', 'is_union_council', 'is_staff',)
    ordering = ('last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    
    def save_model(self, request, obj, form, change):
        if not obj.password:
            user_password = get_random_string(10)
            obj.set_password(user_password)
            super().save_model(request, obj, form, change)

            message_subject = ACCOUNT_VALIDATION_SUBJECT
            html_page = 'users/account_validation_mail.html'
            recipients = obj.email
            email_context = {
                'date': timezone.now(),
                'hostname': request.META['HTTP_HOST'],
                'validation_url': ACCOUNT_VALIDATION_URL,
                'password': user_password,
                'user_name': obj.get_full_name,
                'user_uuid': obj.uuid,
            }            
            generic_send_mail(message_subject, html_page, recipients, email_context)

        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
