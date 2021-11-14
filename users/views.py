#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from global_login_required import login_not_required

from users.forms import ResetPasswordForm, UserLoginForm
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
    
    def get_object(self):
        # To use uuid in the route
        return User.objects.get(uuid=self.kwargs.get('uuid'))

class UpdatePasswordView(SuccessMessageMixin, PasswordChangeView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('password-update-done')
    success_message = 'Votre mot de passe a bien été mis à jour !'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uuid'] = User.objects.get(uuid=self.kwargs.get('uuid'))
        return context

class UpdatePasswordDoneView(PasswordChangeDoneView):
    template_name = "users/change_password_done.html"

@login_not_required
class ResetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = "users/reset_password.html"
    html_email_template_name = 'users/reset_password_mail.html'

@login_not_required
class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "users/reset_password_done.html"

@login_not_required
class ResetPasswordConfirmationView(PasswordResetConfirmView):
    template_name = "users/reset_password_confirmation.html"

@login_not_required
class ResetPasswordCompletedView(PasswordResetCompleteView):
    template_name = "users/reset_password_complete.html"
