# Generated by Django 3.1.1 on 2021-01-14 19:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("founders", "0012_auto_20210114_1922"),
    ]

    operations = [
        migrations.AlterField(
            model_name="progress",
            name="action_helped",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=500), null=True, size=None
            ),
        ),
    ]
