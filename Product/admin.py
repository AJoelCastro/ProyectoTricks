from django.contrib import admin
from .models import Product, Favorite, Color, ProductImage

admin.site.register(Product)
admin.site.register(Favorite)
admin.site.register(Color)
admin.site.register(ProductImage)

# Register your models here.
