from django.shortcuts import render
from Product.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404

def product_list(request, category):
    """Vista genérica para listar productos por categoría"""
    products = Product.objects.filter(category=category)  # Filtrar por categoría
    paginator = Paginator(products, 2)  # 2 productos por página
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, f'Product/product_list_{category}.html', {'products': products})

def product_detail(request, id):
    """Vista para mostrar el detalle de un producto"""
    product = get_object_or_404(Product, id=id)  # Busca el producto y muestra 404 si no existe
    return render(request, 'Product/product_detail.html', {'product': product})