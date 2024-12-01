from django.shortcuts import render
from Product.models import Products_Tendencias, Products_Estiletos
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def menu(request):
    return render(request, 'menu.html', {})

def sandalias(request):
    return render(request, 'sandalias.html', {})

def tendencias(request):
    products = Products_Tendencias.objects.all()
    paginator= Paginator(products, 2)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
    return render(request, 'tendencias.html', {'products': products})

def estiletos(request):
    products = Products_Estiletos.objects.all()
    return render(request, 'estiletos.html', {'products': products})

def tacones(request):
    return render(request, 'tacones.html', {})

def mocasines(request):
    return render(request, 'mocasines.html', {})

def zuecos(request):
    return render(request, 'zuecos.html', {})

def botas(request):
    return render(request, 'botas.html', {})