# from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework import permissions
from core.serializers import TokenSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Token


class TokenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class PurchasedProductsList(generics.ListAPIView):
    """
    Return a list of all the products that the authenticated
    user has ever purchased, with optional filtering.
    """
    model = Token
    serializer_class = TokenSerializer
    # filterset_class = ProductFilter
    

    def get_queryset(self):
        user = self.request.user
        return Token.objects.filter(user=user)


class TokenList(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['token', 'user', 'is_active']