from rest_framework import serializers
from EcommerceWebAPI.apps.user.models import CustomUser, ContactUser


class UserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField("get_email")

    def get_email(self, object):
        contact = ContactUser.objects.filter(user=object).get()
        return contact.email

    phone = serializers.SerializerMethodField("get_phone")

    def get_phone(self, object):
        return ContactUser.objects.filter(user=object).get().phone

    facebook = serializers.SerializerMethodField("get_facebook")

    def get_facebook(self, object):
        return ContactUser.objects.filter(user=object).get().facebook

    address = serializers.SerializerMethodField("get_address")

    def get_address(self, object):
        return ContactUser.objects.filter(user=object).get().address

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "facebook",
            "address",
        ]
