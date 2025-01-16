
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='menu'),
    path('tendencias/', views.tendencias, name='tendencias'),
    path('sandalias/', views.sandalias , name='sandalias' ),
    path('estiletos/', views.estiletos , name='estiletos' ),
    path('tacones/', views.tacones , name='tacones' ),
    path('mocasines/', views.mocasines , name='mocasines' ),
    path('zuecos/', views.zuecos , name='zuecos' ),
    path('botas/', views.botas , name='botas' ),
    path('usuario/', include('usuario.urls')),
    path('favorito/', include('favorito.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('botas/<int:id>/', views.product_detail, name='product_detail'),
]
