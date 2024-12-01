from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu_favoritos(request):
    return render(request, 'menu_favoritos.html', {})

