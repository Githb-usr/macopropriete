#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic.base import TemplateView
from global_login_required import login_not_required

from users.forms import UserLoginForm
from users.settings import LOGIN_ALERT_SUCCESS_MSG

def ValidateUserAccountView(request):
    # récupérer le user à partir du pk
    # vérifier si le user existe et s'il existe, vérifier si son statut est bien "pending"
        # si compte n'existe pas, rediriger vers une page vers une page "échec de la validation de votre compte"
        # si statut déjà validé, rediriger sur la page de login
    # faire passer le statut de pending à validated
    # enregistrer la maj du user
    # rediriger vers la page de validation du compte
    # à partir de cette page, rediriger vers la page de login après qq secondes (JS)
    pass

@login_not_required
class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'

class DashboardView(TemplateView):
    template_name = "users/dashboard.html"
