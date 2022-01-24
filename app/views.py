from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from rest_framework.response import Response
from .models import Profile,User

# Create your views here.


@APIView(['GET'])
def profilelist(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
@APIView(['GET'])
def singleprofile(username, format=None):
        # user = User.objects.filter(username=username).first
        profile=Profile.objects.filter(username=username)
        serializers = ProfileSerializer(profile, many=False)
        return Response(serializers.data)
    
    

