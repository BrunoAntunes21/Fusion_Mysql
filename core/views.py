#importanto a templateview para o uso do class based view
from django.views.generic import TemplateView as TV
from .models import Servico,Funcionario
#criando a classe para a visualizão do template
class IndexView(TV):
    #nomeando o template para a configuração
    template_name = 'index.html '
    #recuperando o contexto da pagina
    def get_context_data(self, **kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        context['servicos']=Servico.objects.order_by('?').all()
        context['funcionarios']=Funcionario.objects.order_by('?').all()
        return context



class NotFoundsView(TV):
    template_name = '404.html'

class ProccesError(TV):
    template_name = '500.html'

