from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import ProfileSerializer,UserSerializer
from rest_framework.response import Response
from .models import Profile,User
from rest_framework import status 
from django.http  import Http404

# Create your views here.

@api_view(['POST']) 
def createuser(request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profilelist( request, format=None):
                all_profiles = Profile.objects.all()
                serializers = ProfileSerializer(all_profiles, many=True)
                return Response(serializers.data)

@api_view(['GET'])
def singleprofile(request,user_id):
        user = User.objects.filter(id=user_id).first()
        profile=Profile.objects.filter(user=user).first()
        serializers = ProfileSerializer(profile, many=False)
        return Response(serializers.data)
@api_view(['PUT'])        
def updateprofile ( request, user_id):
        serializers = ProfileSerializer( request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

