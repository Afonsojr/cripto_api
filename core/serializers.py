from rest_framework import serializers

from core.models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = [
            'id',
            'user',
            'token',
            'quantity',
            'purchase_price',
            'purchased_at',
            'sale_price',
            'sold_at',
            'is_active',
        ]
