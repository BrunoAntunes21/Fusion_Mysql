from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome=forms.CharField(label='nome',max_length=100)
    email=forms.EmailField(label='Email',max_length=100)
    assunto=forms.CharField(label='Assunto',max_length=100)
    menssagem=forms.CharField(label='Menssagem',widget=forms.Textarea())
    #recuperando os dados enviados pelo formulario
    def send_email(self):
        nome=self.cleaned_data['nome']
        email=self.cleaned_data['email']
        assunto=self.cleaned_data['assunto']
        mensagem=self.cleaned_data['menssagem']
        conteudo=f'Nome: {nome} \nEmail: {email}\nAssunto:{assunto}\nMenssagem:{mensagem}'
        #criando o e,ial para ser mandado
        mail=EmailMessage(
            subject=assunto,
            body=conteudo,
            form_email='contato@fusion.com',
            to=['contato@fusion.com',],
            headers={'Reaply-To':email}

        )
        email.send()
