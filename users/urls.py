#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import AccountValidationFailureView, AccountValidationSuccessView, UserLoginView

urlpatterns = [
    path(route='account/validation/<uuid:uuid>', view=views.validate_user_account_view, name='account-validation'),
    path(route='login/', view=UserLoginView.as_view(), name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
    path(route='profile/<uuid:uuid>', view=views.ProfileView.as_view(), name='profile'),
    path(route='profile/<uuid:uuid>/edit', view=views.ProfileUpdateView.as_view(), name='profile-update'),
]