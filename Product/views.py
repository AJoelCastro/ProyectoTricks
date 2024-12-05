from django.shortcuts import render
from Product.models import Products_Botas

def product_detail(request, id):
    product = Products_Botas.objects.get(id=id)
    return render(request, 'product_detail.html', {'product':product})