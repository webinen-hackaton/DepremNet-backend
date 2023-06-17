from django.urls import path
from . import apis

urlpatterns = [
    path("all", apis.UserListApi.as_view(), name="get_all_user"),
    path("<int:id>/", apis.UserByIdApi.as_view(), name="user_by_id"),
    path("<int:pk>/photo", apis.UserPhotoApi.as_view(), name="user_by_id_photo"),
]
