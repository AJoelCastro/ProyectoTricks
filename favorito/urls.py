from django.urls import path, include
from . import views

urlpatterns = [
    path('menu_favoritos/', views.menu_favoritos, name="menu_favoritos"),
    path('accounts/', include('django.contrib.auth.urls')),
]