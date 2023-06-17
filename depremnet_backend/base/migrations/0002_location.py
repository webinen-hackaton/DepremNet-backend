# Generated by Django 4.2.2 on 2023-06-17 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geolocation_fields.models.fields


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_user_team_id"),
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("location", geolocation_fields.models.fields.PointField()),
                ("last_updated_date", models.DateTimeField()),
            ],
        ),
    ]
