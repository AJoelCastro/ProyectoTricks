from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.product_detail, name='product_detail'),
]