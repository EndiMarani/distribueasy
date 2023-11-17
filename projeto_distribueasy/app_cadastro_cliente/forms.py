from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['tipo_cliente','cliente_cpf_cnpj','cliente_nome', 'cliente_email','cliente_telefone','cliente_telefone2','cliente_rua','cliente_bairro','cliente_cidade','cliente_estado','cliente_numero_casa','cliente_complemento','cliente_cep']
        labels = {
            'tipo_cliente': 'Tipo',
            'cliente_cpf_cnpj':'Documento',
            'cliente_nome':'Nome',
            'cliente_email':'E-mail',
            'cliente_telefone':'Telefone',
            'cliente_telefon2':'Segundo Telefone',
            'cliente_rua':'Rua',
            'cliente_bairro':'Bairro',
            'cliente_cidade':'Cidade',
            'cliente_estado':'Estado',
            'cliente_numero_casa':'Número',
            'cliente_complemento':'Complemento',
            'cliente_cep':'CEP',            
        }