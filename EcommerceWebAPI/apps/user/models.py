from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def __str__(self):
        return self.username


class ContactUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def delete(self):
        pass

    def __str__(self):
        return self.user.username
