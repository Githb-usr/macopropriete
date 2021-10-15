#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import UserLoginView

urlpatterns = [
    path(route='account/<int:pk>/validate', view=views.ValidateUserAccountView, name='account-validation'),
    path(route='login/', view=UserLoginView.as_view(), name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
    path(route='dashboard/', view=views.DashboardView.as_view(), name='dashboard'),
]