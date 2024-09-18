from enum import Enum

class GenderEnum(Enum):
    MALE = "Male"
    FEMALE = "Female"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class StatusEnum(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class UserRoleEnum(Enum):
    RIDER = "Rider"
    TENANT = "Tenant"
    ADMIN = "Admin"
    EMPLOYEE = "Employee"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)