from django.db import models

# Create your models here.

class alunos(models.Model):

    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    curso = models.CharField('Curso', max_length=100)
    dataNascimento = models.DateField('Data de Nascimento')
    cpf = models.IntegerField('CPF')
    rg = models.CharField('RG', max_length=100)
    dataIngresso = models.DateField('Data de Ingresso')
    foto = models.CharField('Foto', max_length=100)

    def __str__(self):
        return self.nome
