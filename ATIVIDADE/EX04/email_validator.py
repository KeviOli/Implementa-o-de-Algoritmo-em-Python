import re

def is_valid_email(email):
    # Padrão de expressão regular para validar e-mails
    pattern = r'^[\w\.-]+@[a-zA-Z\d]+\.[a-zA-Z]{2,}$'
    
    # Verifica se o e-mail corresponde ao padrão
    if re.match(pattern, email):
        return True
    else:
        return False
