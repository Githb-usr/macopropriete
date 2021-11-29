#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import ResetPasswordView, ResetPasswordDoneView,\
    ResetPasswordConfirmationView, ResetPasswordCompletedView,\
    UpdatePasswordView, UpdatePasswordDoneView, UserLoginView

urlpatterns = [
    path(
        route='account/validation/<uuid:uuid>',
        view=views.validate_user_account_view,
        name='account-validation',
    ),
    path(
        route='login/',
        view=UserLoginView.as_view(),
        name='login',
    ),
    path(
        route='logout/',
        view=LogoutView.as_view(),
        name='logout',
    ),
    path(
        route='password/reset',
        view=ResetPasswordView.as_view(),
        name='password-reset',
    ),
    path(
        route='password/reset/done',
        view=ResetPasswordDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        route='password/reset/confirmation/<uidb64>/<token>/',
        view=ResetPasswordConfirmationView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        route='password/reset/complete',
        view=ResetPasswordCompletedView.as_view(),
        name='password_reset_complete',
    ),
    path(
        route='password/update/<uuid:uuid>',
        view=UpdatePasswordView.as_view(),
        name='password-update'
    ),
    path(
        route='password/update/done',
        view=UpdatePasswordDoneView.as_view(),
        name='password-update-done',
    ),
    path(
        route='profile/<uuid:uuid>',
        view=views.ProfileView.as_view(),
        name='profile',
    ),
    path(
        route='profile/<uuid:uuid>/edit',
        view=views.ProfileUpdateView.as_view(),
        name='profile-update'
    ),
]
