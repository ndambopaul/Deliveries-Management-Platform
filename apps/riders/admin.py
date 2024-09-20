from django.contrib import admin
from apps.riders.models import Rider


# Register your models here.
@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "user", "tenant"]
