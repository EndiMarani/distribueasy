from django.db import models

# Create your models here.
class Cliente(models.Model):
    cliente_CHOICE = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica')
    )
    tipo_cliente = models.CharField(max_length=2, choices=cliente_CHOICE)
    cliente_cpf = models.CharField(max_length=14)
    cliente_cnpj = models.CharField(max_length=18)
    cliente_nome = models.CharField(max_length=50)
    cliente_nome_empresa = models.CharField(max_length=50)
    cliente_email = models.EmailField(max_length=50)
    cliente_telefone = models.CharField(max_length=14)
    cliente_telefone2 = models.CharField(max_length=14, blank=True, null=True)
    cliente_rua = models.CharField(max_length=50)
    cliente_bairro = models.CharField(max_length=50)
    cliente_cidade = models.CharField(max_length=50)
    estado_CHOICE = (
        ('AC','Acre'),
        ('AL','Alagoas'),
        ('AP','Amapá'),
        ('AM','Amazonas'),
        ('BA','Bahia'),
        ('CE','Ceará'),
        ('DF','Distrito Federal'),
        ('ES','Espírito Santo'),
        ('GO','Goiás'),
        ('MA','Maranhão'),
        ('MT','Mato Grosso'),
        ('MS','Mato Grosso do Sul'),
        ('MG','Minas Gerais'),
        ('PA','Pará'),
        ('PB','Paraíba'),
        ('PE','Pernambuco'),
        ('PI','Piauí'),
        ('RJ','Rio de Janeiro'),
        ('RN','Rio Grande do Norte'),
        ('RS','Rio Grande do Sul'),
        ('RO','Rondônia'),
        ('RR','Roraima'),
        ('SC','Santa Catarina'),
        ('SP','São Paulo'),
        ('SE','Sergipe'),
        ('TO','Tocantins')
    )
    cliente_estado = models.CharField(max_length=2,choices=estado_CHOICE)
    cliente_numero_casa = models.CharField(max_length=10)
    cliente_complemento = models.CharField(max_length=50)
    cliente_cep = models.CharField(max_length=18)
    cliente_data_registro = models.DateTimeField(auto_now_add=True)
    cliente_data_edicao = models.DateTimeField(auto_now_add=True)