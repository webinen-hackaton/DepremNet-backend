from django.urls import path
from . import apis

urlpatterns = [
    path("new", apis.PostCreateApi.as_view(), name="create_new_post"),
    path("<int:pk>", apis.PostByIdApi.as_view(), name="post_by_id"),
]
