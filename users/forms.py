#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm,\
    UserCreationForm, UserChangeForm

from users.models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Create new user by staff
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password',)

class CustomUserChangeForm(UserChangeForm):
    """
    Update user by staff
    """
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields

class UserLoginForm(AuthenticationForm):
    """
    User login
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

class ResetPasswordForm(PasswordResetForm):
    """
    Password reset
    """
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        # Disable email labels
        self.fields["email"].label = ""

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'login-form-input',
            'placeholder': 'Votre email de connexion',
            'id': 'login-id'
        }
    ))

class ProfileUpdateForm(forms.ModelForm):
    """
    Profile update
    """
    class Meta:
        model = User
        fields = ('avatar', 'about', 'contact_email', 'phone_number')
