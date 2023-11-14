from rest_framework import viewsets
from .models import ShoppingCartItem
from .serializers import ShoppingCartItemSerializer

class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer
