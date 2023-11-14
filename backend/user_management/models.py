from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    # Add your custom fields here
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    class Meta:
        permissions = [
            # Define custom permissions if needed
        ]

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
    )
