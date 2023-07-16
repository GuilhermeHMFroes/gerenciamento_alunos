# Generated by Django 4.2.3 on 2023-07-16 06:12

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('curso', models.CharField(max_length=100, verbose_name='Curso')),
                ('dataNascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('rg', models.CharField(max_length=100, verbose_name='RG')),
                ('dataIngresso', models.DateField(verbose_name='Data de Ingresso')),
                ('foto', stdimage.models.StdImageField(force_min_size=False, upload_to='alunos', variations={'thumb': (124, 124)}, verbose_name='Foto')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
        ),
    ]
