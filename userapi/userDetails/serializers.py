# users/serializers.py
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from . import models


class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True,max_length=10,min_length=10)
    password1 = serializers.CharField(write_only=True)
    age = serializers.CharField(required=True, max_length=3, min_length=1)

    class Meta:
        model = models.AppUser
        fields = ('email','first_name','last_name','phone', 'password1', 'age')

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
            'password1': self.validated_data.get('password1', ''),
            'age': self.validated_data.get('age', '')
        }

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AppUser
        fields = ('email','first_name','last_name','phone', 'age')
        #read_only_fields = ('email',)