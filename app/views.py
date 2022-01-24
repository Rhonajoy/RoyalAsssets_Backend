from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ProfileSerializer,UserSerializer
from rest_framework.response import Response
from .models import Profile,User
from rest_framework.response import status 

# Create your views here.
class user:
       @APIView(['POST']) 
       def postuser(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class profile:
        @APIView(['GET'])
        def profilelist(self, request, format=None):
                all_profiles = Profile.objects.all()
                serializers = ProfileSerializer(all_profiles, many=True)
                return Response(serializers.data)
        @APIView(['GET'])
        def singleprofile(username, format=None):
                user = User.objects.filter(username=username).first
                profile=Profile.objects.filter(user=user)
                serializers = ProfileSerializer(profile, many=False)
                return Response(serializers.data)
        
        

