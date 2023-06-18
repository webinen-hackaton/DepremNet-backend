
from rest_framework import (
    views, 
    response, 
    exceptions
)

from rest_framework import generics
from . import models, serializers, services
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CreateEventApi(generics.CreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventCreateSerializer

class EventApi(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class LocationApi(generics.GenericAPIView):
    
    def post(self, request):

        token = request.headers.get("Authorization")
        _id = services.parse_jwt_id(token)
        user = UserModel.objects.filter(id=_id).first()

        serializer = serializers.LocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        location = models.Location(
            person=user,
            location=data["location"],
        )

        location.save()

        return response.Response(data={"message": "new location saved to db"})

class LocationByIdApi(generics.RetrieveUpdateAPIView):
    # authentication_classes = (user_authentication.CustomAuthentication, )
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer