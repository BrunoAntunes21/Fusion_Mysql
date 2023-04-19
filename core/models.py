from django.db import models
import uuid
from stdimage import StdImageField
def get_file_path(instance,filename):
    ext=filename.split('.')[-1]
    filename=f'{uuid.uuid4()}.{ext}'
    return filename


# Create your models here. criação de um modelo de dados base
class Base(models.Model):
    criacao=models.DateField('Data de criação',auto_now_add=True),
    modificado=models.DateField('Atualização',auto_now=True),
    ativo=models.BooleanField('Ativo?',default=True),

    class Meta:
        abstract=True
    def __str__(self):
        return self.criacao
        return self.modificdo
        return self.ativo

class Servico(Base):
    ICONE_CHOICES={
        ('lni-cog','Engrenagem'),
        ('lni-statis-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layer', 'design'),
        ('lni-mobile', 'mobile'),
        ('lni-rocket', 'foguete'),
    }
    servico=models.CharField('Servico',max_length=100)
    descricao=models.TextField('descricao',max_length=200)
    icone=models.CharField('icone',max_length=100,choices=ICONE_CHOICES)

    class Meta:
        verbose_name='Serviço',
        verbose_name_plural='Serviços'

    def __str__(self):
        return self.servico




class Cargo(Base):
    cargo=models.CharField('Cargo',max_length=100)
    class Meta:
        verbose_name='Cargo'
        verbose_name_plural='cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome=models.CharField('Nome',max_length=100)
    cargo=models.ForeignKey('core.Cargo',verbose_name='Cargo',on_delete=models.CASCADE)
    bio=models.TextField('Bio',max_length=200)
    imagem=StdImageField('Imagem',upload_to=get_file_path,variations={'thumb':{'width':480,'height':480}})
    facebook = models.CharField('Facebook',max_length=100,default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    class Meta:
        verbose_name='Funcionario'
        verbose_name_plural="Funcionarios"

    def __str__(self):
        return self.nome
