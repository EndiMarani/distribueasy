from django.urls import path
from .views import *

urlpatterns = [
    path('entrada', tela_entrada, name='tela_entrada'),
    path('usuarios/listar', listar_usuarios, name='listar_usuarios'),
    path('usuarios/listar/<int:id>',listar_usuarios_id, name='listar_usuarios_id'),
    path('usuarios/editar/<int:id>', editar_usuarios, name='editar_usuarios'),
    path('usuarios/excluir/<int:id>', excluir_usuarios, name='excluir_usuarios'),
    path('cadastro', cadastrar_usuarios, name='cadastrar_usuarios'),

]