# Generated by Django 4.2.2 on 2023-06-17 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0003_team_team_members"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="team_status",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team_status",
                to="team.status",
            ),
        ),
    ]
