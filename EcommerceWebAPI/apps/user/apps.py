from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "EcommerceWebAPI.apps.user"

    def ready(self):
        import EcommerceWebAPI.apps.user.signals
