# contador_de_palavras.py

def contar_palavras(texto):
    # Quebra o texto em palavras e conta
    palavras = texto.split()
    return len(palavras)

def main():
    print("Bem-vindo ao Contador de Palavras!")
    
    # Solicita ao usuário um texto
    texto = input("Digite um texto para contar as palavras: ")
    
    # Conta as palavras
    total_palavras = contar_palavras(texto)
    
    print(f"O total de palavras no seu texto é: {total_palavras}")

if __name__ == "__main__":
    main()
