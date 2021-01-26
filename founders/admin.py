from django.contrib import admin

# Register your models here.
from .models import Founder, Progress


class FounderAdmin(admin.ModelAdmin):
    pass


class ProgressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Founder, FounderAdmin)
admin.site.register(Progress, ProgressAdmin)
