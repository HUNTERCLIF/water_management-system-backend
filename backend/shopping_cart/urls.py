from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ShoppingCartItemViewSet

router = DefaultRouter()
router.register(r'shopping-cart-items', ShoppingCartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
