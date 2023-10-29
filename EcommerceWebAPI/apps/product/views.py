from django.shortcuts import render
from rest_framework import viewsets
from EcommerceWebAPI.apps.product.serializers import ProductSerializer
from EcommerceWebAPI.apps.product.models import Product


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
