
from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from .models import Post

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        read_only_fields=["id"]
        exclude=["password"]

class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Post
        exclude=["post_created_date", ]

class PostSerializer(serializers.ModelSerializer):
    
    person = UserSerializer(many=False, read_only = True)

    class Meta:
        model=Post
        fields="__all__"
        # read_only_fields = ["id"]