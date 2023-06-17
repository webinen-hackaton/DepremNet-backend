from django.db import models
from django.contrib.auth import get_user_model
import secrets

UserModel = get_user_model()

def user_directory_path(instance, filename):
    url_safe_token = secrets.token_urlsafe()
    return 'media/user_{0}/{1}'.format(instance.id, url_safe_token)

# Create your models here.
class Post(models.Model):
    person = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="person_post"
    ),
    post_description = models.TextField(max_length=1000)
    post_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True, default=None)
    post_created_date = models.DateTimeField(auto_now_add=True)
