# Generated by Django 4.2.2 on 2023-06-17 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("team", "0004_alter_team_team_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="team_manager",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team_manager",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
