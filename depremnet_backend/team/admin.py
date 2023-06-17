from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Team)
admin.site.register(models.TeamType)
admin.site.register(models.Status)
admin.site.register(models.Job)