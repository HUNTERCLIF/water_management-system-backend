from rest_framework import serializers
from .models import ShoppingCartItem

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('id', 'user', 'product', 'quantity')
