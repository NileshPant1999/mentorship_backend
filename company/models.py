from django.db import models

# Create your models here.
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=100)
    author = models.CharField(max_length=244)
    text = models.CharField(max_length=500)
    image_link = models.CharField(
        max_length=255,
        default="""https://global-uploads.webflow.com/
                   5f4b9ee5f40a6467ebb252ce/5fd1fd23349ab9cc8
                   612d7be_Customers_resource%20library.png""",
    )

    def __str__(self):
        return self.author


class CompanyDetails(models.Model):
    startup_name = models.CharField(max_length=150)
    website = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=300)
    is_launched = models.BooleanField(default=False)
    app_link = models.CharField(max_length=200)
    video_link = models.CharField(max_length=100)
    TIME_CHOICES = (
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("20", "20"),
    )
    time_commitment = models.CharField(
        max_length=100, choices=TIME_CHOICES, default="Part Time"
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ceo",
    )

    def __str__(self):
        return self.startup_name
