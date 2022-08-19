from django.contrib import admin

# Register your models here.
from .models import Token


class TokenAdmin(admin.ModelAdmin):

    list_display = ['user', 'token', 'quantity', 'purchase_price', 'purchased_at', 'sale_price', 'sold_at', 'is_active']
    list_filter = ['user', 'token', 'quantity', 'purchase_price', 'purchased_at', 'sale_price', 'sold_at', 'is_active']
    search_fields = ['user', 'token', 'quantity', 'purchase_price', 'purchased_at', 'sale_price', 'sold_at', 'is_active']


admin.site.register(Token, TokenAdmin)