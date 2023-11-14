from django.db import models
from product_catalog.models import Product
from django.contrib.auth import get_user_model



class ShoppingCartItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Add more fields as needed

    def __str__(self):
        return f"Shopping Cart Item {self.id}"
