from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite
from Product.models import Product

@login_required
def menu_favoritos(request):
    favorites = Favorite.objects.filter(user=request.user)
    print("favorites", favorites[0].product.id)
    return render(request, 'list.html', {'favorites': favorites})

def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.create(user=request.user, product=product)
    return redirect('menu_favoritos')

def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    return redirect('menu_favoritos')

