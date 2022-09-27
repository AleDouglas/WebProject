from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.forms import widgets
from stdimage.models import StdImageField

# Create your models here.

from django.db.models import signals #Antes de inserir os dados nos bancos ele faz algo antes com esses dados
from django.template.defaultfilters import slugify #Ele pega o título do 'produto' e cria uma url

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de modificação', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

def slug_pre_save(signal, instance, sender, **kwargs): #Antes de salvar no banco de dados vai rodar isso
    instance.slug = slugify(instance.nome) #Ele pega o nome de algo e transforma, por exemplo, Maria Mole para maria-mole para poder transformar isso em URL


class Post(models.Model):
    thumbnail = models.ImageField('Thumbnail', upload_to='BlogMedia')
    title = models.CharField('Título', max_length = 200)
    description = models.CharField('Descrição', max_length = 500)
    text = models.TextField('Texto')

    def __str__(self):
        return self.title