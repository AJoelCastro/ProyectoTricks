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
        'TENDENCIAS': products_tendencias,
        'ESTILETOS': products_estiletos,
        'SANDALIAS': products_sandalias,
        'TACONES': products_tacones,
        'MOCASINES': products_mocasines,
        'ZUECOS': products_zuecos,
        'BOTAS': products_botas,
    }
    print(data['TENDENCIAS'])
    return render(request, 'menu.html', data)

