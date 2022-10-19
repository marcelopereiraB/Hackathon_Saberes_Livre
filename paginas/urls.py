from django.urls import path
from .views import PaginaInicial, Vaquinha, Ajuda
#tm que ser urlpatterns pq é padrão django
urlpatterns = [
    # path('endereço/', minhaview.as_view(), name = 'nome-da-url'),
    path('', PaginaInicial.as_view(), name = 'index'),
    path('vaquinha/', Vaquinha.as_view(), name = 'vaquinha'),
    path('ajuda/', Ajuda.as_view(), name = 'ajuda')
]
