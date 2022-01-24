from rest_framework import serializers
from .models import Profile,User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('')
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'full_name', 'username','role')