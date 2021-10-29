#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from global_login_required import login_not_required

from users.forms import UserLoginForm
from users.models import User

@login_not_required
def validate_user_account_view(request, uuid):
    # récupérer le user à partir du uuid
    try:
        user = User.objects.get(uuid=uuid)
        if user.status == 'VALIDATED':
            # si statut déjà validé, rediriger sur la page de login
            return redirect('login')
        elif user.status == 'PENDING':
            # sinon faire passer le statut de pending à validated
            user.status = 'VALIDATED'
            user.save()
            return redirect('account-validation-success')
    except ObjectDoesNotExist:
        return redirect('account-validation-failure')

@login_not_required
class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'

@login_not_required
class AccountValidationFailureView(TemplateView):
    template_name = 'users/account_validation_failure.html'

@login_not_required
class AccountValidationSuccessView(TemplateView):
    template_name = 'users/account_validation_success.html'

class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        # To use uuid in the route
        return User.objects.get(uuid=self.kwargs.get("uuid"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uuid'] = self.kwargs.get("uuid")
        return context

class ProfileUpdateView(UpdateView):
    model = User
    fields = ['avatar', 'about', 'contact_email', 'phone_number']
    template_name = 'users/profile_update.html'
    success_url = 'edit/success'
    
    def get_object(self, queryset=None):
        # To use uuid in the route
        return User.objects.get(uuid=self.kwargs.get("uuid"))

class ProfileUpdateSuccessView(TemplateView):
    template_name = 'users/profile_update_success.html'
