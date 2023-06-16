
from rest_framework import (
    views, 
    response, 
    exceptions,
    permissions
)

from .. import serializers as user_serializer

from .. import services as user_services
from .. import authentication as user_authentication

class UserByIdApi(views.APIView):
    authentication_classes = (user_authentication.CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, id):
        user = user_services.user_id_selector(id)

        if user is None:
            raise ValueError("with given credentials user does not exists")
        
        serializer = user_serializer.UserSerializer(user)

        resp = response.Response(data=serializer.data)
        return resp
    
    def put(self, request, id):

        serializer = user_serializer.UpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        user = user_services.user_id_selector(id)

        if not user:
            raise ValueError("no user found in db")
        
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.phone_number = data["phone_number"]

        user.save()

        return response.Response(data={"message": f"user data changed successfully: {user.id}"})