#from pyexpat import model
from rest_framework import serializers
from .models import  User,Profile,RequestAsset,Asset
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email','password')
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("pk", 'full_name', 'user','role','profile_photo') 
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=RequestAsset
        fields = '__all__'
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asset
        fields = '__all__'



        

class UserProfileChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    