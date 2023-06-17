# Generated by Django 4.2.2 on 2023-06-17 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="team_status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team_status",
                to="team.status",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="team_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team_type",
                to="team.teamtype",
            ),
        ),
    ]
