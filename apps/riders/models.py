from django.db import models

from apps.core.models import AbstractBaseModel
# Create your models here.
class Rider(AbstractBaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.SET_NULL, null=True)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
