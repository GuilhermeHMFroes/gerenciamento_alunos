from django import forms
from django.core.mail.message import EmailMessage
from .models import alunos

class alunoModelForm(forms.ModelForm):
    class Meta:
        model = alunos
        fields = ['nome', 'idade', 'curso', 'dataNascimento', 'cpf', 'rg', 'dataIngresso', 'foto']
