from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['tipo_cliente','cliente_cpf','cliente_cnpj','cliente_nome', 'cliente_nome_empresa','cliente_email','cliente_telefone','cliente_telefone2','cliente_rua','cliente_bairro','cliente_cidade','cliente_estado','cliente_numero_casa','cliente_complemento','cliente_cep']
        labels = {
            'tipo_cliente': 'Tipo',
            'cliente_cpf':'CPF',
            'cliente_cnpj':'CNPJ',
            'cliente_nome':'Nome',
            'cliente_nome_empresa':'Empresa',
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
    
    def clean(self):
        cleaned_data = super().clean()
        tipo_cliente = cleaned_data.get('tipo_cliente')

        if tipo_cliente == 'PF':
            if not cleaned_data.get('cliente_cpf'):
                self.add_error('cliente_cpf', 'Este campo é obrigatório para Pessoa Física.')
            if not cleaned_data.get('cliente_nome'):
                self.add_error('cliente_nome', 'Este campo é obrigatório para Pessoa Física.')
        elif tipo_cliente == 'PJ':
            if not cleaned_data.get('cliente_cnpj'):
                self.add_error('cliente_cnpj', 'Este campo é obrigatório para Pessoa Jurídica.')
            if not cleaned_data.get('cliente_nome_empresa'):
                self.add_error('cliente_nome_empresa', 'Este campo é obrigatório para Pessoa Jurídica.')