# Generated by Django 3.1.1 on 2021-01-07 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Founder",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("mobile", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=30)),
                ("linkedin", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="founder",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
