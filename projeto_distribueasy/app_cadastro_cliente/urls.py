from django.urls import path
from .views import *

urlpatterns = [
    path('entrada', tela_entrada, name='tela_entrada'),
    path('listar', listar_usuarios, name='listar_usuarios'),
    path('cadastro', cadastrar_usuarios, name='cadastrar_usuarios'),
]