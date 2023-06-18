from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserModel
        exclude=["password", ]

class EventCreateSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), )

    class Meta:
        model=models.Event
        fields="__all__"
        # exclude=["author", ]

class EventSerializer(serializers.ModelSerializer):

    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model=models.Event
        fields="__all__"

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Location
        fields=["location", "last_updated_date"]
        