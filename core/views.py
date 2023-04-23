#importanto a templateview para o uso do class based view
#no caso tivemos que ttocar de indexview para formview para poder usar o formulario que criamos
from django.views.generic import FormView as FV
from .models import Servico,Funcionario
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages
#criando a classe para a visualizão do template
class IndexView(FV):
    #nomeando o template para a configuração
    template_name = 'index.html '
    #importanto o contato do form
    form_class =ContatoForm
    success_url = reverse_lazy('/')
    #recuperando o contexto da pagina
    def get_context_data(self, **kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        context['servicos']=Servico.objects.order_by('?').all()
        context['funcionarios']=Funcionario.objects.order_by('?').all()
        return context
    def form_valid(self, form,*args,**kwargs):
        form.send_mail()
        messages.success(self.request,'Email enviado com sucesso')
        return super(IndexView,self).form_valid(form,*args,**kwargs)
    def form_invalid(self,form,*args,**kwargs):
        messages.error(self.request,'Erro ao enviar e-mail')
        return super(IndexView,self).form_invalid(form,*args,**kwargs)




class NotFoundsView(FV):
    template_name = '404.html'

class ProccesError(FV):
    template_name = '500.html'


