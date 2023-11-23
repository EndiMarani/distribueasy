import re
from django.core.exceptions import ValidationError
import requests

INVALIDS_CPFS = ("11111111111", "22222222222", "33333333333", "44444444444", "55555555555",
                 "66666666666", "77777777777", "88888888888", "99999999999", "00000000000")

INVALIDS_CNPJS = ("11111111111111", "22222222222222", "33333333333333", "44444444444444", "55555555555555",
                  "66666666666666", "77777777777777", "88888888888888", "99999999999999", "00000000000000")

def digit_generator(cpf_cnpj, weights):
    total = sum(int(cpf_cnpj[i]) * weights[i] for i in range(len(weights)))
    digit = 11 - total % 11
    return 0 if digit > 9 else digit

def validate_cpf_cnpj(value):
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
            raise ValidationError('Número de CPF inválido', 'invalid')
    elif len(cpf_cnpj) == 14:
        # CNPJ validation
        if cpf_cnpj in INVALIDS_CNPJS:
            raise ValidationError('Número de CNPJ inválido', 'invalid')

        weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        first_digit = digit_generator(cpf_cnpj, weights)
        weights.insert(0, 6)
        second_digit = digit_generator(cpf_cnpj, weights)

        if cpf_cnpj[-2:] != f'{first_digit}{second_digit}':
            raise ValidationError('Número de CNPJ inválido', 'invalid')
    else:
        raise ValidationError('CPF ou CNPJ deve conter 11 ou 14 números', 'invalid')


def obter_endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None