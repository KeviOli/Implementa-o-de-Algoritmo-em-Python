# test_phone_validator.py
import pytest
from phone_validator import validate_phone_number

def test_validate_phone_number():
    # Números de telefone válidos
    assert validate_phone_number("(11) 91234-5678") == True
    assert validate_phone_number("(21) 91234-5678") == True
    assert validate_phone_number("(31) 91234-5678") == True
    assert validate_phone_number("(41) 91234-5678") == True
    assert validate_phone_number("(51) 91234-5678") == True

    # Números de telefone inválidos
    assert validate_phone_number("1234567890") == False  # Número sem DDD
    assert validate_phone_number("(AA) 91234-5678") == False  # DDD inválido
    assert validate_phone_number("(11) 81234-5678") == False  # Número inválido
    assert validate_phone_number("(11) 912345678") == False  # Formato inválido
