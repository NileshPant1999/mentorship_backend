from rest_framework import serializers
from .models import Category, CompanyDetails, Post


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = (
            "startup_name",
            "website",
            "about",
            "is_launched",
            "app_link",
            "video_link",
            "customer",
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
