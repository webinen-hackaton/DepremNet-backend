
from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        read_only_fields=["id"]
        exclude=["password"]


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)

    class Meta:
        model=models.Post
        fields=["person", "post_description", "post_image", "post_created_date", ]