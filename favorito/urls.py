from django.urls import path, include
from . import views

urlpatterns = [
    path('menu_favoritos/', views.menu_favoritos, name="menu_favoritos"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]