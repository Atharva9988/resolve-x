from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    organization = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    class Role(models.TextChoices):
        ORG_ADMIN = 'ORG_ADMIN', 'Organization Admin'
        MANAGER = 'MANAGER', 'Manager'
        AGENT = 'AGENT', 'Agent'
        CUSTOMER = 'CUSTOMER', 'Customer'
        

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

    def __str__(self):
        return self.username