from django.db import models

from stdimage import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.

class alunos(models.Model):

    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    curso = models.CharField('Curso', max_length=100)
    dataNascimento = models.DateField('Data de Nascimento')
    cpf = models.BigIntegerField('CPF')
    rg = models.CharField('RG', max_length=100)
    dataIngresso = models.DateField('Data de Ingresso')
    foto = StdImageField('Foto', upload_to='alunos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def aluno_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(aluno_pre_save, sender=alunos)
