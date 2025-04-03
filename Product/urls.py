from django.urls import path
from Product.views import product_list, product_detail

urlpatterns = [
    path('tendencias/', product_list, {'category': 'tendencias'}, name='product_list_tendencias'),
    path('estiletos/', product_list, {'category': 'estiletos'}, name='product_list_estiletos'),
    path('sandalias/', product_list, {'category': 'sandalias'}, name='product_list_sandalias'),
    path('tacones/', product_list, {'category': 'tacones'}, name='product_list_tacones'),
    path('mocasines/', product_list, {'category': 'mocasines'}, name='product_list_mocasines'),
    path('zuecos/', product_list, {'category': 'zuecos'}, name='product_list_zuecos'),
    path('botas/', product_list, {'category': 'botas'}, name='product_list_botas'),
    path('tendencias/<int:id>/', product_detail, {'category': 'tendencias'}, name='product_detail_tendencias'),
    path('estiletos/<int:id>/', product_detail, {'category': 'estiletos'}, name='product_detail_estiletos'),
    path('sandalias/<int:id>/', product_detail, {'category': 'sandalias'}, name='product_detail_sandalias'),
    path('tacones/<int:id>/', product_detail, {'category': 'tacones'}, name='product_detail_tacones'),
    path('mocasines/<int:id>/', product_detail, {'category': 'mocasines'}, name='product_detail_mocasines'),
    path('zuecos/<int:id>/', product_detail, {'category': 'zuecos'}, name='product_detail_zuecos'),
    path('botas/<int:id>/', product_detail, {'category': 'botas'}, name='product_detail_botas'),
]

