from django.contrib import admin
from EcommerceWebAPI.apps.product.models import Product, Category
from EcommerceWebAPI.apps.user.models import CustomUser


# Register your models here.
class ProductField(admin.ModelAdmin):
    list_display = ["name", "desc", "unit_price", "category", "user"]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.filter(is_seller=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Product, ProductField)


class CategoryField(admin.ModelAdmin):
    list_display = ["name", "parent"]


admin.site.register(Category, CategoryField)
