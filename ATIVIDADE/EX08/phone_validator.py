# phone_validator.py
import re

def validate_phone_number(phone_number):
    # Expressão regular para validar números de telefone com DDD
    pattern = r'^\(\d{2}\) 9?\d{4}-\d{4}$'

    # Verificar se o número de telefone corresponde ao padrão
    if re.match(pattern, phone_number):
        return True
    else:
        return False
