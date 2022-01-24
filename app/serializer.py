from rest_framework import serializers
from .models import Profile,User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email','password')
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'full_name', 'user','role')
    def create(self, validated_data):
        profile = Profile.objects.all()
        return profile

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance