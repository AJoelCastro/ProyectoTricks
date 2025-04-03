from django.shortcuts import render
from Product.models import Product

def menu(request):
    products_tendencias = Product.objects.filter(category='tendencias')
    products_estiletos = Product.objects.filter(category='estiletos')
    products_sandalias = Product.objects.filter(category='sandalias')
    products_tacones = Product.objects.filter(category='tacones')
    products_mocasines = Product.objects.filter(category='mocasines')
    products_zuecos = Product.objects.filter(category='zuecos')
    products_botas = Product.objects.filter(category='botas')
    data = {
        'products_tendencias': products_tendencias,
        'products_estiletos': products_estiletos,
        'products_sandalias': products_sandalias,
        'products_tacones': products_tacones,
        'products_mocasines': products_mocasines,
        'products_zuecos': products_zuecos,
        'products_botas': products_botas,
    }
    return render(request, 'menu.html', data)

