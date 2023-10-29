from rest_framework import serializers
from EcommerceWebAPI.apps.product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
