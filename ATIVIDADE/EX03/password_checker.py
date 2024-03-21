import re

def is_secure(password):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(password) < 8:
        return False
    
    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not re.search("[A-Z]", password):
        return False
    
    # Verifica se a senha contém pelo menos uma letra minúscula
    if not re.search("[a-z]", password):
        return False
    
    # Verifica se a senha contém pelo menos um dígito
    if not re.search("[0-9]", password):
        return False
    
    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search("[!@#$%^&*()-_+=]", password):
        return False
    
    return True
