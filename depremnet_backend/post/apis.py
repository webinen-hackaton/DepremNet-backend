
from rest_framework import (
    views, 
    response, 
    exceptions
)

from rest_framework import generics
from . import models, serializers, services
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer
UserModel = get_user_model()

# class PostCreateApi(generics.CreateAPIView):
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.CreatePostSerializer

class PostCreateApi(generics.GenericAPIView):
    
    def post(self, request):

        token = request.headers.get("Authorization")
        _id = services.parse_jwt_id(token)
        user = UserModel.objects.filter(id=_id).first()

        serializer = serializers.CreatePostSerializer(
            data=request.data,
            context={"person":user}
            )
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return response.Response(data=serializer.data)

class PostListApi(generics.ListAPIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-post_created_date')
        serializers = PostSerializer(posts, many=True)
        return response.Response(serializers.data)
    

class PostListByUserApi(generics.GenericAPIView):
    
    def post(self, request):
        token = request.headers.get("Authorization")
        _id = services.parse_jwt_id(token)
        user = UserModel.objects.filter(id=_id).first()

        posts= models.Post.objects.filter(id=user.id).values()
        return response.Response(data=posts)

class PostByIdApi(generics.RetrieveUpdateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


# class PostListApi(views.APIView):

#     def get(self, request):

#         token = request.headers.get("Authorization")
#         _id = services.parse_jwt_id(token)
#         user = UserModel.objects.filter(id=_id).first()


#         qs = models.Post.objects.all()
#         qs = sorted(qs, key=lambda x: x)
