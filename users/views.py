#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from global_login_required import login_not_required

from users.forms import UserLoginForm
from users.models import User

def validate_user_account_view(request, uuid):
    # récupérer le user à partir du uuid
    user = get_object_or_404(User, uuid=uuid)
    # vérifier si le user existe et s'il existe, vérifier si son statut est bien "pending"
    if not user:
        # si compte n'existe pas, rediriger vers une page vers une page "échec de la validation de votre compte"
        return render(request, 'users/account_validation_failure.html')
    elif user.status == 'validated':
        # si statut déjà validé, rediriger sur la page de login
        return render(request, 'users/login.html')
    # faire passer le statut de pending à validated
    user.status = 'validated'
    user.save()
    return render(request, 'users/account_validation_success.html')

@login_not_required
class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'

@login_not_required
class AccountValidationFailureView(TemplateView):
    template_name = "users/account_validation_failure.html"

@login_not_required
class AccountValidationSuccessView(TemplateView):
    template_name = "users/account_validation_success.html"

class Profile(DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        # To use uuid in the route
        return User.objects.get(uuid=self.kwargs.get("uuid"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uuid'] = self.kwargs.get("uuid")
        return context
