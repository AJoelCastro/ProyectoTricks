from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.menu_favoritos, name="menu_favoritos"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]