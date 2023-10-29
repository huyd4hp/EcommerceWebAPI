from rest_framework import serializers
from EcommerceWebAPI.apps.order.models import Cart, DetailCart


class CartSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField("get_payment")

    def get_payment(self, object):
        return object.payment.option

    class Meta:
        model = Cart
        fields = ["id", "total", "quantity", "user", "payment"]


class CartDetailSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField("get_product")

    def get_product(self, object):
        listProduct = []
        detailCart = DetailCart.objects.filter(cart=object)
        for detail in detailCart:
            listProduct.append(DetailCartSerializer(detail).data)
        return listProduct

    class Meta:
        model = Cart
        fields = ["id", "total", "quantity", "user", "payment", "product"]


class DetailCartSerializer(serializers.ModelSerializer):
    unit_price = serializers.SerializerMethodField("get_price")
    id = serializers.SerializerMethodField("get_id")
    name = serializers.SerializerMethodField("get_name")

    def get_id(self, object):
        return object.product.pk

    def get_name(self, object):
        return object.product.name

    def get_price(self, object):
        return object.product.unit_price

    class Meta:
        model = DetailCart
        fields = ["id", "name", "quantity", "unit_price", "addTime"]
