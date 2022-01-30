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
from django.contrib.auth import authenticate, login, logout

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
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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