import re

def validar_senha(senha):
    # Verifica se a senha tem entre 6 e 32 caracteres
    if not 6 <= len(senha) <= 32:
        return "Senha invalida."
    
    # Verifica se a senha contém pelo menos uma letra maiúscula, uma letra minúscula e um número
    if not re.search(r'[A-Z]', senha) or not re.search(r'[a-z]', senha) or not re.search(r'\d', senha):
        return "Senha invalida."
    
    # Verifica se a senha não contém nenhum caractere de pontuação, acentuação ou espaço
    if re.search(r'[^A-Za-z0-9]', senha):
        return "Senha invalida."
    
    # Se passou por todas as verificações, a senha é válida
    return "Senha valida."

# Processamento das entradas
while True:
    try:
        senha = input()
        resultado = validar_senha(senha)
        print(resultado)
    except EOFError:
        break
