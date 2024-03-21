import pytest
from password_checker import is_secure

def test_secure_password():
    assert is_secure("Abcd123!") == True
    assert is_secure("StrongPass@1") == True
    assert is_secure("SecureP@ssw0rd") == True

def test_insecure_password():
    assert is_secure("weak") == False
    assert is_secure("12345678") == False
    assert is_secure("Password") == False
    assert is_secure("password123") == False
    assert is_secure("!@#$%^&*") == False
    assert is_secure("ABCD1234") == False
