from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite
from Product.models import Product
from django.contrib import messages

@login_required
def menu_favoritos(request):
    favorites = Favorite.objects.filter(user=request.user)
    for fav in favorites:
        fav.product.url_name = fav.product.get_url_name()
    return render(request, 'list.html', {'favorites': favorites})

def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Verifica si ya está en favoritos
    if Favorite.objects.filter(user=user, product=product).exists():
        messages.warning(request, 'Este producto ya está en tus favoritos.')
    else:
        Favorite.objects.create(user=user, product=product)
        messages.success(request, 'Producto añadido a favoritos.')
    return redirect('menu_favoritos')

def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    return redirect('menu_favoritos')

