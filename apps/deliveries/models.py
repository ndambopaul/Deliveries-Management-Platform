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


class Delivery(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    rider = models.ForeignKey("riders.Rider", on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("clients.Order", on_delete=models.CASCADE)
    delivery_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    delivery_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)

    def __str__(self):
        return self.order.order_number


class DeliveryStatusUpdate(AbstractBaseModel):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    previous_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)
    next_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)

    def __str__(self):
        return "{self.previous_status} => {self.next_status}"
