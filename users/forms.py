#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from users.models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Form used for create new user by staff
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password',)

class CustomUserChangeForm(UserChangeForm):
    """
    Form used for change user by staff
    """
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields

class UserLoginForm(AuthenticationForm):
    """
    Form used for the user login
    """
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        # Disable login labels
        self.fields["username"].label = ""
        self.fields["password"].label = ""

    username = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'login-form-input',
            'placeholder': 'Identifiant',
            'id': 'login-id'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'login-form-input',
            'placeholder': 'Mot de passe',
            'id': 'login-password',
        }
    ))

class ProfileUpdateForm(forms.ModelForm):
    """
    Form used for the profile update
    """
    class Meta: 
        model = User
        fields = ('avatar', 'about', 'contact_email', 'phone_number')
