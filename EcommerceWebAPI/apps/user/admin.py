from django.contrib import admin
from EcommerceWebAPI.apps.user.models import CustomUser, ContactUser


# Register your models here.
class UserField(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "is_seller"]


admin.site.register(CustomUser, UserField)


class ContactField(admin.ModelAdmin):
    list_display = ["user", "email", "phone", "facebook", "address"]


admin.site.register(ContactUser, ContactField)
