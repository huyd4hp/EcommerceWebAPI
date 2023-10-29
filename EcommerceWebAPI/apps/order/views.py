from django.shortcuts import render
from EcommerceWebAPI.apps.order.models import Cart, DetailCart
from rest_framework.decorators import action
from EcommerceWebAPI.apps.order.serializers import CartSerializer, CartDetailSerializer
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from EcommerceWebAPI.apps.order.models import Order, DetailOrder


# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.filter(~Q(quantity=0))
    serializer_class = CartSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CartSerializer
        elif self.action == "retrieve":
            return CartDetailSerializer
        return CartSerializer

    @action(methods=["POST"], detail=True)
    def pay(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        detailcart = DetailCart.objects.filter(cart=cart)
        if cart.quantity != 0:
            order = Order(
                user=cart.user,
                total=cart.total,
                quantity=cart.quantity,
                payment=cart.payment,
            )
            order.save()
            for detail in detailcart:
                DetailOrder.objects.create(
                    order=order, product=detail.product, quantity=detail.quantity
                )
            detailcart.delete()
            return Response(
                data={
                    "message: Thanh toán thành công",
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            data={
                "message: Thanh toán thất bại",
            },
            status=status.HTTP_200_OK,
        )
