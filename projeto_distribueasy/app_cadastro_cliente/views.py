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

def listar_usuarios_id(request, id):
    usuarios_id = Cliente.objects.get(id=id)
    return render(request, 'usuarios/listar_usuarios_id.html', {'usuarios_id': usuarios_id})

def cadastrar_usuarios(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = ClienteForm()
    return render(request, 'usuarios/cadastrar_usuarios.html', {'form': form})

def editar_usuarios(request, id):
    usuario = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios_id', id=id)
    else:
        form = ClienteForm(instance=usuario)
    return render(request, 'usuarios/cadastrar_usuarios.html', {'form': form, 'editar': True, 'usuario_id': id})


def excluir_usuarios(request,id):
    excluir_usuarios = Cliente.objects.get(id=id)
    if request.method == 'POST':
        excluir_usuarios.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/excluir_usuarios.html', {'excluir_usuarios':excluir_usuarios})