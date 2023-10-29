from django.db import models
from EcommerceWebAPI.apps.user.models import CustomUser
from EcommerceWebAPI.apps.payment.models import Payment
from EcommerceWebAPI.apps.product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    total = models.IntegerField(default=0, editable=False)
    quantity = models.SmallIntegerField(default=0, editable=False)
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, blank=True, null=True, default="1"
    )

    def __str__(self):
        return self.user.username


class DetailCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    addTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart.user.username


class Order(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    total = models.IntegerField()
    quantity = models.SmallIntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.SET_DEFAULT, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class DetailOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.product.name
