from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def CadastroAluno(request):
    return render(request, 'cadastro_aluno.html')

def AlunosCadastrados(request):
    return render(request, 'alunos_cadastrados.html')

