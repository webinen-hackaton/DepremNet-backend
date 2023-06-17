from django.db import models
from geolocation_fields.models import fields
from django.contrib.auth import get_user_model

UserModel = get_user_model() #?

# Create your models here.
class TeamType(models.Model):
    type_name = models.CharField(max_length=50)
    type_description = models.TextField(max_length=200)
    min_member = models.IntegerField()

    def __str__(self):
        return self.type_name

class Status(models.Model): # team status
    status_name = models.CharField(max_length=50)
    status_description = models.TextField(max_length=200)
    status_code = models.IntegerField()

    def __str__(self):
        return self.status_name

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_type = models.ForeignKey(TeamType, on_delete=models.CASCADE, related_name="team_type")
    location = fields.PointField()
    team_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="team_status")
    team_members = models.ManyToManyField(UserModel, related_name='teams')
    
    def __str__(self):
        return self.team_name


class Job(models.Model):
    job_name = models.CharField(max_length=50)
    job_description = models.TextField(max_length=200)

    def __str__(self):
        return self.job_name