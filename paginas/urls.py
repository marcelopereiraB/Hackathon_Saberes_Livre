from django.urls import path
from .views import PaginaInicial, PecaAjuda, Contato, Login, Doar
#tm que ser urlpatterns pq é padrão django
urlpatterns = [
    # path('endereço/', minhaview.as_view(), name = 'nome-da-url'),
    path('', PaginaInicial.as_view(), name = 'index'),
    path('peça_ajuda/', PecaAjuda.as_view(), name = 'peca ajuda'),
    path('contato/', Contato.as_view(), name = 'contato'),
    path('login/', Login.as_view(), name = 'login'),
    path('doar/', Doar.as_view(), name = 'doar'),

]
