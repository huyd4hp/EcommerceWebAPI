from django.shortcuts import render
from EcommerceWebAPI.apps.payment.models import Payment
from EcommerceWebAPI.apps.payment.serializers import PaymentSerializer
from rest_framework import viewsets


# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
