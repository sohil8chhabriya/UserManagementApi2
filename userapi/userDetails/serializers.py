# users/serializers.py
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppUser
        fields = ('email', 'first_name', 'last_name', )