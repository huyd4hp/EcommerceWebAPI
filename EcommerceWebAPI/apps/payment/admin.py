from django.contrib import admin
from EcommerceWebAPI.apps.payment.models import Payment


# Register your models here.
class PaymentField(admin.ModelAdmin):
    list_display = ["option", "desc"]


admin.site.register(Payment, PaymentField)
