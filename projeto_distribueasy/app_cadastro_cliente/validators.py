import re
from django.core.exceptions import ValidationError
import requests

INVALIDS_CPFS = ['12345678909']  # Substitua pela sua lista de CPFs inválidos
INVALIDS_CNPJS = ['12345678901234']  # Substitua pela sua lista de CNPJs inválidos

def digit_generator(cpf_cnpj, weights):
    total = sum(int(cpf_cnpj[i]) * weights[i] for i in range(len(weights)))
    digit = 11 - total % 11
    return 0 if digit > 9 else digit

def validate_cpf_cnpj(value, is_juridica=False):
    cpf_cnpj = re.sub("[^0-9]", "", value)

    if len(cpf_cnpj) == 11:
        # CPF validation
        if cpf_cnpj in INVALIDS_CPFS:
            raise ValidationError('Número de CPF inválido', 'invalid')

        weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        first_digit = digit_generator(cpf_cnpj, weights)
        weights.insert(0, 11)
        second_digit = digit_generator(cpf_cnpj, weights)

        if cpf_cnpj[-2:] != f'{first_digit}{second_digit}':
            raise ValidationError('Número de CPF inválido', 'invalid_cpf')
    elif len(cpf_cnpj) == 14:
        # CNPJ validation
        if cpf_cnpj in INVALIDS_CNPJS:
            raise ValidationError('Número de CNPJ inválido', 'invalid')

        weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        first_digit = digit_generator(cpf_cnpj, weights)
        weights.insert(0, 6)
        second_digit = digit_generator(cpf_cnpj, weights)

        if cpf_cnpj[-2:] != f'{first_digit}{second_digit}':
            raise ValidationError('Número de CNPJ inválido', 'invalid_cnpj')
    else:
        raise ValidationError('CPF ou CNPJ deve conter 11 ou 14 números', 'invalid_length')

    if is_juridica and len(cpf_cnpj) == 11:
        raise ValidationError('Número de CNPJ esperado para pessoa jurídica', 'invalid_length_juridica')
    elif not is_juridica and len(cpf_cnpj) == 14:
        raise ValidationError('Número de CPF esperado para pessoa física', 'invalid_length_fisica')
    
def obter_endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None