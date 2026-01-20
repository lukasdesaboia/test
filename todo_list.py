# todo_list.py

def exibir_lista(tarefas):
    if not tarefas:
        print("Sua lista de tarefas está vazia!")
    else:
        print("\nTarefas pendentes:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    tarefa = input("\nDigite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa(tarefas):
    exibir_lista(tarefas)
    try:
        indice = int(input("\nDigite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número inválido! Nenhuma tarefa removida.")
    except ValueError:
        print("Por favor, insira um número válido.")

def main():
    tarefas = []

    while True:
        print("\n---- Lista de Tarefas ----")
        print("1. Ver tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            exibir_lista(tarefas)
        elif escolha == '2':
            adicionar_tarefa(tarefas)
        elif escolha == '3':
            remover_tarefa(tarefas)
        elif escolha == '4':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
