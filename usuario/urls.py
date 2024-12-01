from django.urls import path, include
from . import views

urlpatterns = [
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
    path('registrarse/', views.registrarse, name="registrarse"),
    path('salir/', views.salir, name="salir"),
    path('accounts/', include('django.contrib.auth.urls')),
]