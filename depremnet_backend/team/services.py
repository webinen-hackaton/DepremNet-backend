from django.contrib.auth import get_user_model
from . import models

UserModel = get_user_model()

def get_team_and_user(team_id:int, user_id:int):
    
    team = models.Team.objects.filter(id=team_id).first()
    user = UserModel.objects.filter(id=user_id).first()

    if not team or not user:
        raise ValueError(f"team or user not exists with given ids: {team_id} - {user_id}")
    
    return team, user