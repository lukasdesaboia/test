# biblioteca.py

class Livro:
    def __init__(self, titulo, autor, ano, status='disponível'):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.ano}) - {self.status}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, ano):
        livro = Livro(titulo, autor, ano)
        self.livros.append(livro)
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Não há livros cadastrados na biblioteca.")
        else:
            print("\nLivros cadastrados:")
            for livro in self.livros:
                print(livro)

    def buscar_por_titulo(self, titulo):
        livros_encontrados = [livro for livro in self.livros if titulo.lower() in livro.titulo.lower()]
        if livros_encontrados:
            for livro in livros_encontrados:
                print(livro)
        else:
            print(f"Nenhum livro encontrado com o título '{titulo}'.")

    def buscar_por_autor(self, autor):
        livros_encontrados = [livro for livro in self.livros if autor.lower() in livro.autor.lower()]
        if livros_encontrados:
            for livro in livros_encontrados:
                print(livro)
        else:
            print(f"Nenhum livro encontrado com o autor '{autor}'.")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and livro.status == 'disponível':
                livro.status = 'emprestado'
                print(f"Livro '{livro.titulo}' emprestado com sucesso!")
                return
        print(f"Livro '{titulo}' não disponível para empréstimo ou não encontrado.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and livro.status == 'emprestado':
                livro.status = 'disponível'
                print(f"Livro '{livro.titulo}' devolvido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado ou não está emprestado.")

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistema de Gerenciamento de Biblioteca ---")
        print("1. Adicionar livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Buscar livro por autor")
        print("5. Emprestar livro")
        print("6. Devolver livro")
        print("7. Sair")
        
        opcao = input("Escolha uma opção (1-7): ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            biblioteca.adicionar_livro(titulo, autor, ano)
        elif opcao == '2':
            biblioteca.listar_livros()
        elif opcao == '3':
            titulo = input("Digite o título para buscar: ")
            biblioteca.buscar_por_titulo(titulo)
        elif opcao == '4':
            autor = input("Digite o autor para buscar: ")
            biblioteca.buscar_por_autor(autor)
        elif opcao == '5':
            titulo = input("Digite o título do livro para emprestar: ")
            biblioteca.emprestar_livro(titulo)
        elif opcao == '6':
            titulo = input("Digite o título do livro para devolver: ")
            biblioteca.devolver_livro(titulo)
        elif opcao == '7':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
