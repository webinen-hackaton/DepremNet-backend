# Generated by Django 4.2.2 on 2023-06-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_alter_location_last_updated_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="location",
            name="person",
        ),
        migrations.AddField(
            model_name="location",
            name="id",
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
