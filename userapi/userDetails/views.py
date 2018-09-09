from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser

from rest_framework import generics

from . import models
from . import serializers

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('first_name', 'last_name', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        fields = UserChangeForm.Meta.fields

class UserListView(generics.ListCreateAPIView):
    queryset = models.AppUser.objects.all()
    serializer_class = serializers.UserSerializer