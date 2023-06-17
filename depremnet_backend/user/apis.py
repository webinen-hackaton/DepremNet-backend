from rest_framework import (
    views, 
    response, 
    exceptions,
    permissions,
    status
    )

from . import serializers as user_serializer
from . import (
    services,
    authentication
    )

from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# class RegisterApi(views.APIView):

#     def post(self, request):
#         serializer = user_serializer.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         data = serializer.validated_data
#         serializer.instance = services.create_user(user_dc=data)

#         return response.Response(data={"message": "new user saved successfully to db"})

class RegisterApi(generics.GenericAPIView):
    serializer_class = user_serializer.RegisterUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginApi(views.APIView):

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        token = services.create_token(user_id=user.id)

        resp = JsonResponse({})
        resp["Authorization"] = token
        return resp

class UserApi(views.APIView):
    authentication_classes = (authentication.CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)

class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        resp = response.Response()
        resp.headers['Authorization'] = ""
        resp.data = {"message": "successfully logged out"}

        return resp
