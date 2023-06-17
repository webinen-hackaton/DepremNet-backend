
from rest_framework import (
    views, 
    response, 
    exceptions
)

from rest_framework import generics
from . import models, serializers

class EventApi(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer