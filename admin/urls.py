from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions, routers

from core.views import PurchasedProductsList, TokenList, TokenViewSet

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version="1.0.0",
        description="API documentation of App",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r"mytokens", TokenViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.authtoken")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("user/", PurchasedProductsList.as_view()),
    path("token/", TokenList.as_view()),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-schema"),
]
