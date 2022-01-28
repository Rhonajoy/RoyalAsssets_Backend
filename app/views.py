from rest_framework.decorators import api_view
from app.serializer import ProfileSerializer,UserSerializer,UserProfileChangeSerializer
from rest_framework.response import Response
from app.models import Profile,User
from rest_framework import status,generics
from django.http  import Http404
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, mixins, permissions

# # Create your views here.
# class UserList(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer 

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer 

# class ProfileList(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer 

@api_view(['POST']) 
def createrequest(request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()

class UserIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UserProfileChangeAPIView(generics.RetrieveAPIView,
                               mixins.DestroyModelMixin,
                               mixins.UpdateModelMixin):
    permission_classes = (
         permissions.IsAuthenticated,
         UserIsOwnerOrReadOnly,
         )
    serializer_class = UserProfileChangeSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def get_object(self):
        
        username = self.kwargs["username"]
        obj = get_object_or_404(User, username=username)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


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

# @api_view(['GET'])
# def singleprofile(request,user_id):
#         user = User.objects.filter(id=user_id).first()
#         profile=Profile.objects.filter(user=user).first()
#         serializers = ProfileSerializer(profile, many=False)
#         return Response(serializers.data)


