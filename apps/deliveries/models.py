from django.db import models

from apps.core.models import AbstractBaseModel

# Create your models here.
DELIVERY_STATUS = (
    ("Created", "Created"),
    ("Dispatched", "Dispatched"),
    ("In Transit", "In Transit"),
    ("Complete", "Complete"),
    ("Pending Dispatch", "Pending Dispatch"),
)

DELIVERY_TYPES = (
    ("Single Order", "Single Order"),
    ("Multiple Orders", "Multiple Orders"),
)


class Delivery(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    rider = models.ForeignKey("riders.Rider", on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("clients.Order", on_delete=models.CASCADE, null=True)
    delivery_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    delivery_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)
    delivery_type = models.CharField(max_length=255, choices=DELIVERY_TYPES, default="Single Order")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.order.order_number if self.order else f"{self.id}"


class DeliveryStatusUpdate(AbstractBaseModel):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    previous_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)
    next_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)

    def __str__(self):
        return "{self.previous_status} => {self.next_status}"


class DeliveryOrder(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    rider = models.ForeignKey("riders.Rider", on_delete=models.SET_NULL, null=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name="deliveryorders")
    order = models.ForeignKey("clients.Order", on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)
    delivery_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.order.order_number