from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def tela_entrada(request):
    return render(request, 'usuarios/tela_entrada.html')

def listar_usuarios(request):
    usuarios = Cliente.objects.all()
    return render(request,'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def cadastrar_usuarios(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = ClienteForm()
    return render(request, 'usuarios/cadastrar_usuarios.html', {'form': form})