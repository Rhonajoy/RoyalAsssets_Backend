from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from app.serializer import ProfileSerializer,UserSerializer,UserProfileChangeSerializer,RequestSerializer,AssetSerializer
from rest_framework.response import Response
from app.models import Profile,User,RequestAsset,Asset
from rest_framework import status,generics
from django.http  import Http404
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .permissions import *
from rest_framework.authtoken.models import Token
# authentication


# login view
class LoginView(APIView):
    """This handles a user login request

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, format=None):
        data = {}
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validate_user()
            # get user token
            token, created = Token.objects.get_or_create(user=user)
            data["token"] = token.key
            responseStatus = status.HTTP_200_OK
            return Response(data, status=responseStatus)

        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(APIView):  # create user
    """
    Create a user.
    """

    # permission_classes = (CreateUserPermission,)
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request, format=None):
        data=request.data
        print (data)
        email=data['email']
        if '@admin' in email:
            role = 1
        elif '@proc_manager' in email:
            role = 2
        else:
            role = 3  

                 
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role=role)
            # return success message
            data = {"message": "User created successfully"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# logout user ====================================
class logoutUser(APIView):  # logout user
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)


# get a single user usign token provided
class GetUser(APIView):
    """
    Get a single user.
    """
    # @swagger_auto_schema(request_body=GetUserSerializer)
    def post(self, request, format=None):
        token = request.data.get("token")
        if token is None:
            data = {"token": "Token is missing 😥"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Token.objects.get(key=token).user
            serializer = GetUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # if token is invalid
        except Token.DoesNotExist:
            data = {"token": "Token is invalid 😥"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


# requests api
@api_view(['POST']) 
def create_request(request, format=None):
        serializers = RequestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def all_requests( request, format=None):
                asset_requests = RequestAsset.objects.all()
                serializers = RequestSerializer(asset_requests, many=True)
                return Response(serializers.data)
@api_view(['GET'])
def single_request(request,request_id):
        asset_request = RequestAsset.objects.filter(id=request_id).first()
        serializers = RequestSerializer(asset_request, many=False)
        return Response(serializers.data)
# assets API
@api_view(['POST']) 
def create_asset(request, format=None):
        serializers = AssetSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def all_assets( request, format=None):
                assets = Asset.objects.all()
                serializers = AssetSerializer(assets, many=True)
                return Response(serializers.data)
@api_view(['GET'])
def single_asset(request,asset_id):
        asset = Asset.objects.filter(id=asset_id).first()
        serializers = Asset(asset, many=False)
        return Response(serializers.data)
        
# update profile api

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




