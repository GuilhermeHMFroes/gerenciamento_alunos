from django.contrib import admin
from .models import alunos

# Register your models here.

@admin.register(alunos)

class alunosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'curso', 'dataNascimento', 'cpf', 'rg', 'dataIngresso', 'slug')
