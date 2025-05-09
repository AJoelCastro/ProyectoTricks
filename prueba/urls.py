
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='menu'),
    path('usuario/', include('usuario.urls')),
    path('favorito/', include('favorito.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include('Product.urls')),
]
