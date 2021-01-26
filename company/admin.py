from django.contrib import admin
from .models import Category, CompanyDetails, Post


class CompanyDetailAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(CompanyDetails, CompanyDetailAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
