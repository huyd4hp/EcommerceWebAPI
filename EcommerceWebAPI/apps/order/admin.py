from django.contrib import admin
from EcommerceWebAPI.apps.order.models import Cart, DetailCart
from EcommerceWebAPI.apps.order.models import Order, DetailOrder


# Register your models here.
class CartField(admin.ModelAdmin):
    list_display = ["user", "total", "quantity", "payment"]


admin.site.register(Cart, CartField)


class DetailCartField(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity", "addTime"]


admin.site.register(DetailCart, DetailCartField)


class OrderField(admin.ModelAdmin):
    list_display = ["user", "total", "quantity", "created_at"]


admin.site.register(Order, OrderField)


class DetailOrderField(admin.ModelAdmin):
    list_display = ["order", "product", "quantity"]


admin.site.register(DetailOrder, DetailOrderField)
