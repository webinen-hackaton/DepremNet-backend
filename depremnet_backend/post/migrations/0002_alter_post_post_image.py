# Generated by Django 4.2.2 on 2023-06-17 09:21

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_image",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to=post.models.user_directory_path,
            ),
        ),
    ]
