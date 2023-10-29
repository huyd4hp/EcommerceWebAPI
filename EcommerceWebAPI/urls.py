from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from EcommerceWebAPI.apps.user import views as UserViews
from EcommerceWebAPI.apps.product import views as ProductViews
from EcommerceWebAPI.apps.payment import views as PayViews
from EcommerceWebAPI.apps.order import views as OrderViews
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce Web API",
        default_version="1.0.1",
        description="Ecommerce Web API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nhathuyd4hp@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r"users", UserViews.UserViewSet, basename="user")
router.register(r"sellers", UserViews.SellerViewSet, basename="seller")
router.register(r"products", ProductViews.ProductViewSet, basename="product list")
router.register(r"payment", PayViews.PaymentViewSet, basename="payment list")
router.register(r"cart", OrderViews.CartViewSet, basename="cart list")
router.register(r"order", OrderViews.OrderViewSet, basename="order list")

urlpatterns = [
    # ---------------------------
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # ---------------------------
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
