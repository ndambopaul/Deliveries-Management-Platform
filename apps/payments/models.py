from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
class RiderEarning(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    rider = models.ForeignKey("riders.Rider", on_delete=models.CASCADE)
    month = models.CharField(max_length=255)
    year = models.IntegerField()
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    redeemed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.month}, {self.year}"


class RiderPayment(AbstractBaseModel):
    earning = models.ForeignKey(RiderEarning, on_delete=models.CASCADE)
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    rider = models.ForeignKey("riders.Rider", on_delete=models.CASCADE)
    delivery = models.ForeignKey("deliveries.Delivery", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    redeemed = models.BooleanField(default=False)

    def __str__(self):
        return self.rider.user.username

class RiderPayout(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    rider = models.ForeignKey("riders.Rider", on_delete=models.CASCADE)
    earning = models.ForeignKey(RiderEarning, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return self.rider.user.username

class ClientInvoice(AbstractBaseModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    month = models.CharField(max_length=255)
    year = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=200, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=200, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.client.name} Invoice for {self.month}, {self.year}"


class DeliveryPayments(AbstractBaseModel):
    invoice = models.ForeignKey(ClientInvoice, on_delete=models.CASCADE)
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    delivery = models.ForeignKey("deliveries.Delivery", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.client.name