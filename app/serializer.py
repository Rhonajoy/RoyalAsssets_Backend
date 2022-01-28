#from pyexpat import model
from rest_framework import serializers
from .models import  User,Profile
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
        model=



        

class UserProfileChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    