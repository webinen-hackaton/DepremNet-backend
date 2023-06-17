# Generated by Django 4.2.2 on 2023-06-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_description", models.TextField(max_length=1000)),
                (
                    "post_image",
                    models.ImageField(blank=True, null=True, upload_to="uploads/"),
                ),
                ("post_created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
