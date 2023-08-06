from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserAccount

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        name = self.validated_data["name"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        account = User(name=name, email=email, password=password)
        account.set_password(password)
        account.save()
        return account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email")
