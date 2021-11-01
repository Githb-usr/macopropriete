#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from global_login_required import login_not_required

from users.forms import UserLoginForm
from users.models import User
from users.settings import ACCOUNT_DOES_NOT_EXIST, ALREADY_VALIDATED_ACCOUNT_MSG, VALIDATED_ACCOUNT_SUCCESS_MSG

@login_not_required
def validate_user_account_view(request, uuid):
    try:
        user = User.objects.get(uuid=uuid)
        if user.status == 'VALIDATED':
            messages.success(request, ALREADY_VALIDATED_ACCOUNT_MSG)
            return redirect('login')
        elif user.status == 'PENDING':
            user.status = 'VALIDATED'
            user.save()
            messages.success(request, VALIDATED_ACCOUNT_SUCCESS_MSG)
            return redirect('login')
    except ObjectDoesNotExist:
        messages.error(request, ACCOUNT_DOES_NOT_EXIST)
        return redirect('login')

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

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ['avatar', 'about', 'contact_email', 'phone_number']
    template_name = 'users/profile_update.html'
    success_message = 'Votre profil a bien été mis à jour !'
    
    def get_object(self, queryset=None):
        # To use uuid in the route
        return User.objects.get(uuid=self.kwargs.get("uuid"))
