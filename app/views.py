from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from rest_framework.response import Response
from .models import Profile

# Create your views here.

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
