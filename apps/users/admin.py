from django.contrib import admin
from apps.users.models import User
# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "username", "email", "role", "tenant"]