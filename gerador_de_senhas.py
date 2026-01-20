# gerador_de_senhas.py
import random
import string

def gerar_senha(tamanho=12):
    # Definir os caracteres que podem aparecer na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas Aleatórias!")
    
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
    exce
