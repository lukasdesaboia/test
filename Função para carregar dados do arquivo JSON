import json
import os

# Função para carregar dados do arquivo JSON
def carregar_dados():
    if os.path.exists('dados.json'):
        with open('dados.json', 'r') as f:
            return json.load(f)
    return {"usuarios": {}, "tarefas": {}}

# Função para salvar dados no arquivo JSON
def salvar_dados(dados):
    with open('dados.json', 'w') as f:
        json.dump(dados, f, indent=4)

# Função de autenticação do usuário
def autenticar_usuario(dados):
    while True:
        print("\n---- Autenticação ----")
        acao = input("Você deseja [1] Registrar ou [2] Login? (1/2): ")
        
        if acao == '1':  # Registrar novo usuário
            username = input("Escolha um nome de usuário: ")
            if username in dados['usuarios']:
                print("Usuário já existe. Tente outro nome.")
            else:
                senha = input("Escolha uma senha: ")
                dados['usuarios'][username] = senha
                dados['tarefas'][username] = []
                salvar_dados(dados)
                print(f"Usuário {username} registrado com sucesso!")
                return username
        
        elif acao == '2':  # Login de usuário existente
            username = input("Digite seu nome de usuário: ")
            if username in dados['usuarios']:
                senha = input("Digite sua senha: ")
                if dados['usuarios'][username] == senha:
                    print(f"Bem-vindo, {username}!")
                    return username
                else:
                    print("Senha incorreta. Tente novamente.")
            else:
                print("Usuário não encontrado. Tente novamente.")
        else:
            print("Opção inválida! Tente novamente.")

# Função para exibir as tarefas de um usuário
def exibir_tarefas(usuario, dados):
    tarefas = dados['tarefas'].get(usuario, [])
    if tarefas:
        print("\n--- Tarefas ---")
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - {status}")
    else:
        print("Você não tem tarefas no momento.")

# Função para adicionar uma nova tarefa
def adicionar_tarefa(usuario, dados):
    descricao = input("Digite a descrição da tarefa: ")
    dados['tarefas'][usuario].append({"descricao": descricao, "concluida": False})
    salvar_dados(dados)
    print("Tarefa adicionada com sucesso!")

# Função para marcar uma tarefa como concluída
def marcar_concluida(usuario, dados):
    exibir_tarefas(usuario, dados)
    try:
        num_tarefa = int(input("Digite o número da tarefa para marcar como concluída: "))
        tarefa = dados['tarefas'][usuario][num_tarefa - 1]
        tarefa['concluida'] = True
        salvar_dados(dados)
        print("Tarefa marcada como concluída!")
    except (ValueError, IndexError):
        print("Número de tarefa inválido. Tente novamente.")

# Função para remover uma tarefa
def remover_tarefa(usuario, dados):
    exibir_tarefas(usuario, dados)
    try:
        num_tarefa = int(input("Digite o número da tarefa para remover: "))
        dados['tarefas'][usuario].pop(num_tarefa - 1)
        salvar_dados(dados)
        print("Tarefa removida com sucesso!")
    except (ValueError, IndexError):
        print("Número de tarefa inválido. Tente novamente.")

# Função para o menu de tarefas
def menu_tarefas(usuario, dados):
    while True:
        print("\n---- Gerenciador de Tarefas ----")
        print("1. Ver tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4/5): ")

        if opcao == '1':
            exibir_tarefas(usuario, dados)
        elif opcao == '2':
            adicionar_tarefa(usuario, dados)
        elif opcao == '3':
            marcar_concluida(usuario, dados)
        elif opcao == '4':
            remover_tarefa(usuario, dados)
        elif opcao == '5':
            print("Saindo do gerenciador de tarefas. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Função principal do sistema
def sistema():
    dados = carregar_dados()
    usuario = autenticar_usuario(dados)
    menu_tarefas(usuario, dados)

if __name__ == "__main__":
    sistema()
