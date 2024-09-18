from django.contrib import admin
from apps.clients.models import Order, OrderStatusUpdate, Client
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "client", "tenant", "customer_name", "order_status"]


@admin.register(OrderStatusUpdate)
class OrderStatusUpdateAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "order", "previous_status", "next_status"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "name", "tenant", "phone_number", "website"]
