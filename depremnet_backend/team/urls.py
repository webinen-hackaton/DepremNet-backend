from django.urls import path

from . import apis

urlpatterns = [
    # path("/", None, name="team_apis"),
    # path("<id:int>/", None, name="team_by_id"),
    # path("<id:int>/update", None, name="team_update_by_id"),
    # path("<id:int>/delete", None, name="team_delete_by_id"),
    # path("all/", None, name="team_all"),
    # path("create/", None, name="team_create"),
    path('', apis.TeamApi.as_view(), name='teams'),
    path('<int:team_id>', apis.TeamByIdApi.as_view(), name='team-detail'),
]
