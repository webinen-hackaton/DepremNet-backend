from django.urls import path
from . import apis

urlpatterns = [
    path("event", apis.EventApi.as_view(), name="event")
]
