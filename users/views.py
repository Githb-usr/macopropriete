#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from global_login_required import login_not_required

from users.forms import UserLoginForm
from users.models import User
from config.settings import EMAIL_HOST_USER, RECIPIENT_ADDRESS

def generic_send_mail(subject, message):
    send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[RECIPIENT_ADDRESS],
            fail_silently=False,
        )

def validate_user_account_view(request, uuid):
    # récupérer le user à partir du uuid
    user = get_object_or_404(User, uuid=uuid)
    # vérifier si le user existe et s'il existe, vérifier si son statut est bien "pending"
    if not user:
        # si compte n'existe pas, rediriger vers une page vers une page "échec de la validation de votre compte"
        return render(request, 'account_validation_failure.html')
    elif user.status == 'Validated':     
        # si statut déjà validé, rediriger sur la page de login
        return render(request, 'login.html')
    # faire passer le statut de pending à validated
    user.status = 'Validated'
    # enregistrer la maj du user
    user.save()
    # rediriger vers la page de validation du compte
    return render(request, 'account_validation_successful.html')
    # à partir de cette page, rediriger vers la page de login après qq secondes (JS)

@login_not_required
class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'

class DashboardView(TemplateView):
    template_name = "users/dashboard.html"

@login_not_required
class AccountValidationFailureView(TemplateView):
    template_name = "users/account_validation_failure.html"

@login_not_required
class AccountValidationSuccessView(TemplateView):
    template_name = "users/account_validation_success.html"
