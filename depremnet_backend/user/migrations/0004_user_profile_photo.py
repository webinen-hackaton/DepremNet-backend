# Generated by Django 4.2.2 on 2023-06-16 23:31

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_user_is_staff"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                blank=True, null=True, upload_to=user.models.user_directory_path
            ),
        ),
    ]
