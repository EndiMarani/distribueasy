# forms.py
from django import forms
from .models import Cliente
from .validators import *


class ClienteForm(forms.ModelForm):
    cliente_estado = forms.CharField(label='Estado', required=False)
    cliente_municipio = forms.CharField(label='Município', required=False)

    class Meta:
        model = Cliente
        fields = ['tipo_cliente', 'cliente_cpf_cnpj', 'cliente_nome', 'cliente_email', 'cliente_telefone', 'cliente_telefone2', 'cliente_rua', 'cliente_bairro', 'cliente_cidade', 'cliente_estado', 'cliente_municipio', 'cliente_numero_casa', 'cliente_complemento', 'cliente_cep', 'cliente_categoria']
    
    widgets = {
        'cliente_cpf_cnpj': forms.TextInput(attrs={'class': 'form-control only-digits'}),
        # Adicione outros widgets conforme necessário para os outros campos
    }
    
    cliente_categoria = forms.ChoiceField(choices=Cliente.categoria_CHOICES, widget=forms.RadioSelect)
 
    
    def clean_cliente_cep(self):
        cep = self.cleaned_data['cliente_cep']
        
        informacoes_endereco = obter_endereco(cep)

        if not informacoes_endereco:
            raise forms.ValidationError('CEP inválido ou não encontrado', code='invalid_cep')

        # Atualize os campos do endereço no formulário
        self.cleaned_data['cliente_cidade'] = informacoes_endereco.get('localidade', '')
        self.cleaned_data['cliente_estado'] = informacoes_endereco.get('uf', '')
        self.cleaned_data['cliente_bairro'] = informacoes_endereco.get('bairro', '')
        self.cleaned_data['cliente_rua'] = informacoes_endereco.get('logradouro', '')

        return cep

    
    def clean(self):
        cleaned_data = super().clean()
        tipo_cliente = cleaned_data.get('tipo_cliente')
        cliente_cpf_cnpj = cleaned_data.get('cliente_cpf_cnpj')

        if tipo_cliente and cliente_cpf_cnpj:
            validate_cpf_cnpj(cliente_cpf_cnpj)

        # Adicione outras validações conforme necessário

        return cleaned_data
    
    
