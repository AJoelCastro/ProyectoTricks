from django.urls import path
from Product.views import product_list

urlpatterns = [
    path('tendencias/', product_list, {'category': 'tendencias'}, name='product_list_tendencias'),
    path('estiletos/', product_list, {'category': 'estiletos'}, name='product_list_estiletos'),
    path('sandalias/', product_list, {'category': 'sandalias'}, name='product_list_sandalias'),
    path('tacones/', product_list, {'category': 'tacones'}, name='product_list_tacones'),
    path('mocasines/', product_list, {'category': 'mocasines'}, name='product_list_mocasines'),
    path('zuecos/', product_list, {'category': 'zuecos'}, name='product_list_zuecos'),
    path('botas/', product_list, {'category': 'botas'}, name='product_list_botas'),
]

