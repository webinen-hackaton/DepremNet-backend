from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.
class Post(models.Model):
    person = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="person_post"
    ),
    post_description = models.TextField(max_length=1000)
    post_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    post_created_date = models.DateTimeField(auto_now_add=True)
