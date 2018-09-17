from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser
from django.http import JsonResponse
from rest_framework.views import APIView
import logging
logger = logging.getLogger(__name__)
from rest_framework import generics

from . import models
from . import serializers

from rest_auth.registration.views import RegisterView

class CustomRegisterView(RegisterView):

    serializer_class = serializers.CustomRegisterSerializer
    queryset = models.AppUser.objects.all()
    #serializer_class = serializers.CustomRegisterSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = models.AppUser.objects.all()
    serializer_class = serializers.CustomUserDetailsSerializer
