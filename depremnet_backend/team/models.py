from django.db import models
from geolocation_fields.models import fields

# Create your models here.
class TeamType(models.Model):
    type_name = models.CharField(max_length=50)
    type_description = models.TextField(max_length=200)
    min_member = models.IntegerField()

class Status(models.Model):
    pass

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_type = models.ForeignKey(TeamType, on_delete=models.DO_NOTHING)
    location = fields.PointField(verbose="location")
    team_status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.team_name


class Job(models.Model):
    job_name = models.CharField(max_length=50)
    job_description = models.TextField(max_length=200)

    def __str__(self):
        return self.job_name