#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

class UserLoginForm(auth_forms.AuthenticationForm):
    """
    Form used for the user login
    """
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

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
