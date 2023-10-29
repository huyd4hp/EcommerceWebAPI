from django.db.models.signals import post_save, pre_delete

from django.dispatch import receiver
from EcommerceWebAPI.apps.order.models import Cart, DetailCart
from EcommerceWebAPI.apps.user.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_contact_user(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


@receiver(pre_delete, sender=DetailCart)
def update_total_cart(sender, instance, **kwargs):
    cart = instance.cart
    product = instance.product
    cart.total -= product.unit_price * instance.quantity
    cart.quantity -= instance.quantity
    cart.save()


@receiver(post_save, sender=DetailCart)
def update_total_cart(sender, instance, created, **kwargs):
    if created:
        cart = instance.cart
        product = instance.product
        cart.total += product.unit_price * instance.quantity
        cart.quantity += instance.quantity
        cart.save()
