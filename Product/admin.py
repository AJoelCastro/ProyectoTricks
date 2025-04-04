from django.contrib import admin
from .models import Product, Color, ProductImage

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(ProductImage)

# Register your models here.
