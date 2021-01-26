from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timedelta

# Create your models here.


class Founder(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    linkedin = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="founder"
    )

    def __str__(self):
        return self.first_name


class Progress(models.Model):
    numberof_stakeholder = models.IntegerField(null=True, default=0)
    learning_stakeholder = models.TextField(null=True, default="Hi")
    mentor_feedback = models.TextField(null=True)
    coach_feedback = models.TextField(null=True)
    goals = ArrayField(models.CharField(max_length=500), null=True)
    action_helped = ArrayField(models.CharField(max_length=500), null=True)
    learning_conversation = models.TextField(null=True)
    unplanned_action_help = models.TextField(null=True)
    primary_metric = models.IntegerField(default=1234)
    lastweek_metric = models.IntegerField(null=True, default=12)
    target_market = models.CharField(null=True, default="hi", max_length=250)
    top_priorities = models.TextField(null=True, default="hi")
    conversation = models.IntegerField(default=45)
    start_date = models.CharField(
        max_length=255,
        default=(
            datetime.now().date() - timedelta(days=datetime.now().date().weekday())
        ),
    )
    end_date = models.CharField(
        max_length=255,
        default=(
            (datetime.now().date() - timedelta(days=datetime.now().date().weekday()))
            + timedelta(days=6)
        ),
    )
    slug = models.SlugField(max_length=250, null=True, blank=True, default="112321")
    founder_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Progress"
    )
