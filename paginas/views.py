from django.views.generic import TemplateView

#criando 

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'
class PecaAjuda(TemplateView):
    template_name = 'paginas/peça_ajuda.html'
class Contato(TemplateView):
    template_name = 'paginas/contato.html'
class Login(TemplateView):
    template_name = 'paginas/login.html'
class Doar(TemplateView):
    template_name = 'paginas/doar.html'
