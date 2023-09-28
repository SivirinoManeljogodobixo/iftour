from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from comentario.models import Avaliacao
from .models import Bloco, Piso, Sala, Administrador
from django.contrib.auth.models import User


def index(request):
    lista = Bloco.objects.all()
    return render(request, 'index.html', {"lista" : lista})


def add_bloco(request):
    return render(request, 'add_bloco.html')

def sala(request,id):
    s = Sala.objects.get(pk=id)
    comentarios = Avaliacao.objects.filter(sala = s)
    soma = 0
    for c in comentarios:
        soma += c.nota
    if len(comentarios) > 0:
        media = soma/len(comentarios)
    else:
        media = 0

    ctx = {
        'bloco' : s.piso.bloco,
        'piso' : s.piso,
        'sala' : s,
        'comentarios' : comentarios,
    }
    return render(request, 'sala.html',ctx)

def bloco(request, id):
    b = Bloco.objects.get(pk=id)
    blocos = Bloco.objects.all()
    pisos = Piso.objects.filter(bloco=b)
    ctx = {
        'bloco' : b,
        'blocos': blocos,
        'pisos' : pisos
    }
    return render(request, 'bloco.html', ctx)

def blocodefault(request):
    b = Bloco.objects.all()[0]
    print(b)
    return redirect(f'/bloco/{b.id}/')


# Create your views here.
def piso(request, id):
    p = Piso.objects.get(pk=id)
    pisos = Piso.objects.filter(bloco=p.bloco)
    salas = Sala.objects.filter(piso = p)
    ctx = {
        'blocos' : Bloco.objects.all(),
        'bloco' : p.bloco,
        'pisos' : pisos,
        'piso' : p,
        'salas' :salas
    }
    return render(request, 'bloco.html', ctx)

def cadastro_adm(request):
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']
        email = request.POST['email']
        foto = request.FILES.get('foto')

        # Verifica se o usuário já existe
        if User.objects.filter(username=login).exists():
            print("nome de usuário já existente")
            pass
        else:
            # Cria o usuário e registra com adm
            user = User.objects.create_user(username=login, password=senha, email=email)
            administrador = Administrador(login=user, nome=login, email=email, senha=senha, foto=foto)
            administrador.save()

        user = authenticate(request, username=login, password=senha)
        if user is not None:
            login(request, user)
            return redirect('login_adm')
    else:
        # manda para o cadastro de adm
        form = UserCreationForm()
    return render(request, 'cadastro_adm.html', {'form': form})

def login_adm(request):
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']
        user = authenticate(request, username=login, password=senha)
        if user is not None:
            login(request, user)
            return redirect('#') #dhasbord do administrador.
        else:
            print("Login ou senha incorretos")
            pass
    return render(request, 'login_adm.html')