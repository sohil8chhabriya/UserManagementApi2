# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser

class AppUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('first_name', 'last_name', 'email', 'password')

class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        fields = UserChangeForm.Meta.fields