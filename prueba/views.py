from django.shortcuts import render
from Product.models import Products_Tendencias, Products_Estiletos, Products_Botas, Products_Mocasines, Products_Sandalias, Products_Tacones, Products_Zuecos
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def menu(request):
    return render(request, 'menu.html', {})

def sandalias(request):
    products = Products_Sandalias.objects.all()
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'sandalias.html', {'products':products})

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
    paginator= Paginator(products, 2)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
    return render(request, 'estiletos.html', {'products': products})

def tacones(request):
    products = Products_Tacones.objects.all()
    paginator= Paginator(products, 2)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
    return render(request, 'tacones.html', {'products': products})

def mocasines(request):
    products = Products_Mocasines.objects.all()
    paginator= Paginator(products, 2)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
    return render(request, 'mocasines.html', {'products': products})

def zuecos(request):
    products = Products_Zuecos.objects.all()
    paginator= Paginator(products, 2)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
    return render(request, 'zuecos.html', {'products': products})

def botas(request):
    products = Products_Botas.objects.all()
    paginator= Paginator(products, 2)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
    return render(request, 'botas.html', {'products': products})
