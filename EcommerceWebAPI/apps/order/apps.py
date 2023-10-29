from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "EcommerceWebAPI.apps.order"

    def ready(self):
        import EcommerceWebAPI.apps.order.signals
