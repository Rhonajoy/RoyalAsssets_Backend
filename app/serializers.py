from rest_framework import fields, serializers, validators
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    """This defines working with the user roles table

    Args:
        serializers ([type]): [description]
    """

    class Meta:
        model = Role
        fields = "__all__"
        read_only_fields = ["name"]


# login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate_user(self):
        user = authenticate(
            username=self.validated_data["username"],
            password=self.validated_data["password"],
        )
        if user is None:
            raise serializers.ValidationError("Invalid Credentials")
        return user


# get user serializer
class GetUserSerializer(serializers.ModelSerializer):
    # role = RoleSerializer(read_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role"]


# create user
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name","password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# get a single user usign token
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
class Add_staffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_staff
        fields = ("id","username","contact","department")        