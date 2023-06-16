from django.urls import path
from . import apis

urlpatterns = [
    path("<int:id>/", apis.UserByIdApi.as_view(), name="user_by_id")
]