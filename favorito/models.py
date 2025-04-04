from django.db import models
from django.contrib.auth.models import User
from Product.models import Product

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Evita duplicados

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
