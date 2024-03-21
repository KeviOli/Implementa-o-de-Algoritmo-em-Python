# word_counter.py

import re

def count_words(text):
    # Usar uma expressão regular para encontrar todas as palavras no texto
    words = re.findall(r'\b\w+\b', text)
    # Retornar o número de palavras encontradas
    return len(words)
