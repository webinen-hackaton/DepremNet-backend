from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

from . import services

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    profile_photo = serializers.ImageField()
    phone_number = serializers.CharField()
    nationality_id = serializers.CharField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.UserDataClass(**data)
    
class UpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()

class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model=UserModel
        read_only_fields=["id"]
        exclude=["profile_photo"]

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

class UserImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserModel
        fields=['profile_photo', ]
