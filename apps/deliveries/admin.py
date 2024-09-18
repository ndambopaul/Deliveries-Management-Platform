from django.contrib import admin
from apps.deliveries.models import Delivery
# Register your models here.
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["id", "tenant", "order", "rider", "delivery_cost", "delivery_status"]
