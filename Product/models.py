from django.db import models
from django.contrib.auth.models import User

class Color(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    codeHexadecimal = models.CharField(max_length=7, default='#000000', blank=False, null=False)

    def __str__(self):
        return self.name

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

    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    color = models.ManyToManyField(Color)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tendencias', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")  # Relación 1 a N
    image_url = models.URLField(blank=False, null=False)

    def __str__(self):
        return f"Imagen de {self.product.name}"
    
    