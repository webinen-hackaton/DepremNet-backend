from django.urls import path
from . import apis

urlpatterns = [
    path("new", apis.PostCreateApi.as_view(), name="create_new_post"),
    path("me", apis.PostListByUserApi.as_view(), name="get_posts_by_user"),
    path("<int:pk>", apis.PostByIdApi.as_view(), name="post_by_id"),
]
