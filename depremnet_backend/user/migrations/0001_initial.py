# Generated by Django 4.2.2 on 2023-06-16 15:36

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Last Name"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Email"
                    ),
                ),
                ("password", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=12, unique=True)),
                ("nationality_id", models.CharField(max_length=11, unique=True)),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
    ]