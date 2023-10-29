from django.db import models
from EcommerceWebAPI.apps.user.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.parent}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    unit_price = models.IntegerField()
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
