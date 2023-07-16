from django.shortcuts import render

from .forms import alunoModelForm
from django.contrib import messages
from .models import alunos

# Create your views here.

def index(request):
    return render(request, 'index.html')

def CadastroAluno(request):
    if request.method == 'POST':
        form = alunoModelForm(request.POST, request.FILES)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.save()  # Salvar o objeto aluno no banco de dados

            messages.success(request, 'Aluno cadastrado com sucesso')

        else:
            messages.error(request, 'Erro ao cadastrar o aluno')
            print(form.errors)

    else:
        form = alunoModelForm()

    context = {
        'form': form
    }

    return render(request, 'cadastro_aluno.html', context)


def AlunosCadastrados(request):
    context = {
        'alunos': alunos.objects.all()
    }

    return render(request, 'alunos_cadastrados.html', context)

