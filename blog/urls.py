from django.urls import path

from .models import Kartochka
from .views import EslatmalarViewSet, KartochkaViewSet

eslatma_list = EslatmalarViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

eslatma_detail = EslatmalarViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
kartochka_list = KartochkaViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

kartochka_detail = KartochkaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})




urlpatterns = [
    path('eslatmalar/', eslatma_list, name='eslatma-list'),
    path('eslatmalar/<int:pk>/', eslatma_detail, name='eslatma-detail'),
    path('kartochka/', kartochka_list, name='eslatma-list'),
    path('kartochka/<int:pk>/', kartochka_detail, name='eslatma-detail'),
]
