from django.urls import path
from . import apis

urlpatterns = [
    path("event/create", apis.CreateEventApi.as_view(), name="event"),
    path("event/", apis.EventApi.as_view()),
    path("location/create", apis.LocationApi.as_view(), name="location"),
    path("location/<int:pk>", apis.LocationByIdApi.as_view(), name="location_by_id"),
]
