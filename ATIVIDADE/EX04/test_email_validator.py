import pytest
from email_validator import is_valid_email

def test_valid_emails():
    assert is_valid_email("user@example.com") == True
    assert is_valid_email("john.doe@example.com") == True
    assert is_valid_email("jane.doe123@example.com") == True
    assert is_valid_email("user123@example.com") == True

def test_invalid_emails():
    assert is_valid_email("invalid_email") == False
    assert is_valid_email("user@example") == False
    assert is_valid_email("user.example.com") == False
    assert is_valid_email("user@example_com") == False
