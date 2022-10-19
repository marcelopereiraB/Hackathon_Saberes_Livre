from django.views.generic import TemplateView

#criando 
class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'
class Vaquinha(TemplateView):
    template_name = 'paginas/vaquinha.html'
class Ajuda(TemplateView):
    template_name = 'paginas/help.html'