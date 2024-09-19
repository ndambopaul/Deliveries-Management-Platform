from django.db import models
from apps.core.models import AbstractBaseModel


# Create your models here.
class Tenant(AbstractBaseModel):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
