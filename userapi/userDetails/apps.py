# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AppUserCreationForm, AppUserChangeForm
from .models import AppUser

class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ['email', 'first_name', 'last_name']

admin.site.register(AppUser, AppUserAdmin)

class UserdetailsConfig(AppConfig):
    name = 'userDetails'
