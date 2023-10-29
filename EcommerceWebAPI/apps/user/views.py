from django.shortcuts import render
from rest_framework import viewsets
from EcommerceWebAPI.apps.user.serializers import UserSerializer
from EcommerceWebAPI.apps.user.models import CustomUser


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_active=True, is_seller=False)
    serializer_class = UserSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_active=True, is_seller=True)
    serializer_class = UserSerializer
