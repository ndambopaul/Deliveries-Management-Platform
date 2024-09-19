from django.db import models

from apps.core.models import AbstractBaseModel


# Create your models here.
class Client(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


ORDER_STATUSES = (
    ("Created", "Created"),
    ("Pending Dispatch", "Pending Dispatch"),
    ("Dispatched", "Dispatched"),
    ("Delivered", "Delivered"),
    ("Set For Delivery", "Set For Delivery"),
)


class Order(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="clientorders"
    )
    order_number = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_location = models.JSONField(null=True)
    customer_address = models.CharField(max_length=500)
    order_status = models.CharField(
        max_length=255, choices=ORDER_STATUSES, default="Pending Dispatch"
    )
    delivery_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return self.order_number


class OrderStatusUpdate(AbstractBaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="orderstatuses"
    )
    previous_status = models.CharField(max_length=255, choices=ORDER_STATUSES)
    next_status = models.CharField(max_length=255, choices=ORDER_STATUSES)

    def __str__(self):
        return f"{self.previous_status} => {self.next_status}"
