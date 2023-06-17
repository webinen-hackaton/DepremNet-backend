from rest_framework import serializers
from . import models

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Event
        fields="__all__"

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Location
        fields=["location", "last_updated_date"]
        