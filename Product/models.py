from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tendencias', 'Tendencias'),
        ('estiletos', 'Estiletos'),
        ('sandalias', 'Sandalias'),
        ('tacones', 'Tacones'),
        ('mocasines', 'Mocasines'),
        ('zuecos', 'Zuecos'),
        ('botas', 'Botas'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tendencias')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Evita duplicados

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"