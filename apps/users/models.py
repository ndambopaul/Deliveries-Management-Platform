from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import AbstractBaseModel
from apps.core.constants import GenderEnum, UserRoleEnum


# Create your models here.
class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(max_length=255, choices=UserRoleEnum.choices())
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=255, choices=GenderEnum.choices())
    id_number = models.CharField(max_length=255, null=True)
    kra_pin = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to="users/", null=True)
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def name(self):
        return f"{self.first_name} {self.last_name}"
