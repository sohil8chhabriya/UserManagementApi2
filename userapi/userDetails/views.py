from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import AppUser

from rest_framework import generics

from . import models
from . import serializers

class AppUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('first_name', 'last_name', 'email')

class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        fields = UserChangeForm.Meta.fields

class UserListView(generics.ListCreateAPIView):
    queryset = models.AppUser.objects.all()
    serializer_class = serializers.UserSerializer

class RegisterFormView(APIView):
    def post(self, request, format=None):
        user = models.AppUser.objects.all()
        email = request.data.get("email", None)
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        password = request.data.get('password1', None)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = password

        try:
            user.save()
            return JsonResponse({'status': 1, 'message': 'User registered successfully!'})
        except:
            return JsonResponse({'status': 0, 'message': 'There was something wrong while registering the user.'})