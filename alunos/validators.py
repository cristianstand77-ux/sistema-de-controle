import re
from django.core.exceptions import ValidationError


def validar_cpf(value):
    cpf = re.sub(r'\D', '', value or '')

    if len(cpf) != 11:
        raise ValidationError('O CPF deve conter 11 dígitos.')

    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido.')

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    if digito1 != int(cpf[9]):
        raise ValidationError('CPF inválido.')

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    if digito2 != int(cpf[10]):
        raise ValidationError('CPF inválido.')

    return cpf