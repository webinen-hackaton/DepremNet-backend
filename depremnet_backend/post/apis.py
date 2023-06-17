
from rest_framework import (
    views, 
    response, 
    exceptions
)

from rest_framework import generics
from . import models, serializers, services
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PostCreateApi(generics.CreateAPIView):
    queryset = models.Post
    serializer_class = serializers.PostSerializer

class PostByIdApi(generics.RetrieveUpdateAPIView):
    queryset = models.Post
    serializer_class = serializers.PostSerializer

class PostListApi(views.APIView):

    def get(self, request):

        token = request.data["access_token"]
        _id = services.parse_jwt_id(token)
        user = UserModel.objects.filter(id=_id).first()


        qs = models.Post.objects.all()
        qs = sorted(qs, key=lambda x: x)