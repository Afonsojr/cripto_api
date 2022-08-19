from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.views import TokenViewSet, PurchasedProductsList, TokenList


router = routers.DefaultRouter()
router.register(r'mytokens', TokenViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('user/', PurchasedProductsList.as_view()),
    path('token/', TokenList.as_view()),

]