from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions,viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User



class RegisterViewset(viewsets.ModelViewSet):

     queryset = User.objects.all().order_by('-date_joined')
     serializer_class = RegisterSerializer
     authentication_classes = (TokenAuthentication,)
     permission_classes =(IsAuthenticated,)







    



