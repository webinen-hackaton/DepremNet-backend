from django.db import models
from geolocation_fields.models import fields
from django.contrib.auth import get_user_model

from geolocation_fields.models import fields

UserModel = get_user_model()

# Create your models here.
class Event(models.Model):
    author = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )
    title = models.CharField(verbose_name="title", max_length=50)
    description = models.TextField(verbose_name="description", default="", max_length=255)
    location = fields.PointField()
    radius = models.FloatField()
    created_date = models.DateTimeField(verbose_name='created_date')
    is_active = models.BooleanField(verbose_name="is_active", default=False)

    def __str__(self) -> str:
        return f"{self.title}, ({self.created_date})"
    

class Location(models.Model):
    location = fields.PointField()
    last_updated_date = models.DateTimeField(auto_now=True)