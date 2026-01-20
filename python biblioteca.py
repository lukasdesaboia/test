#python biblioteca.py
import json
import os
from datetime import datetime

ARQUIVO = "biblioteca.json"

# ---------- DADOS ----------

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "usuarios": {},
        "livros": {},
        "emprestimos": []
    }

def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# ---------- USUÁRIOS ----------

def registrar_usuario(dados):
    usuario = input("Usuário: ")
    if usuario in dados["usuarios"]:
        print("Usuário já existe.")
        return
    senha = input("Senha: ")
    dados["usuarios"][usuario] = senha
    salvar_dados(dados)
    print("Usuário registrado com sucesso!")

def login(dados):
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if dados["usuarios"].get(usuario) == senha:
        print(f"Bem-vindo, {usuario}!")
        return usuario
    print("Login inválido.")
    return None

# ---------- LIVROS ----------

def cadastrar_livro(dados):
    codigo = input("Código do livro: ")
    if codigo in dados["livros"]:
        print("Livro já cadastrado.")
        return
    titulo = input("Título: ")
    autor = input("Autor: ")
    dados["livros"][codigo] = {
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    }
    salvar_dados(dados)
    print("Livro cadastrado com sucesso!")

def listar_livros(dados):
    if not dados["livros"]:
        print("Nenhum livro cadastrado.")
        return
    for cod, livro in dados["livros"].items():
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"[{cod}] {livro['titulo']} - {livro['autor']} ({status})")

# ---------- EMPRÉSTIMOS ----------

def emprestar_livro(dados, usuario):
    listar_livros(dados)
    codigo = input("Código do livro: ")
    livro = dados["livros"].get(codigo)

    if not livro:
        print("Livro não encontrado.")
        return
    if not livro["disponivel"]:
        print("Livro já está emprestado.")
        return

    livro["disponivel"] = False
    dados["emprestimos"].append({
        "usuario": usuario,
        "codigo": codigo,
        "data": datetime.now().strftime("%d/%m/%Y")
    })
    salvar_dados(dados)
    print("Livro emprestado com sucesso!")

def devolver_livro(dados, usuario):
    emprestimos_usuario = [
        e for e in dados["emprestimos"] if e["usuario"] == usuario
    ]

    if not emprestimos_usuario:
        print("Você não tem empréstimos.")
        return

    for i, e in enumerate(emprestimos_usuario, 1):
        livro = dados["livros"][e["codigo"]]
        print(f"{i}. {livro['titulo']} ({e['data']})")

    try:
        escolha = int(input("Escolha: ")) - 1
        emprestimo = emprestimos_usuario[escolha]
    except:
        print("Opção inválida.")
        return

    dados["livros"][emprestimo["codigo"]]["disponivel"] = True
    dados["emprestimos"].remove(emprestimo)
    salvar_dados(dados)
    print("Livro devolvido com sucesso!")

def historico(usuario, dados):
    print("\n--- Histórico ---")
    for e in dados["emprestimos"]:
        if e["usuario"] == usuario:
            livro = dados["livros"][e["codigo"]]
            print(f"{livro['titulo']} - {e['data']}")

# ---------- MENUS ----------

def menu_usuario(usuario, dados):
    while True:
        print("""
1. Listar livros
2. Emprestar livro
3. Devolver livro
4. Meu histórico
5. Sair
""")
        op = input("Opção: ")

        if op == "1":
            listar_livros(dados)
        elif op == "2":
            emprestar_livro(dados, usuario)
        elif op == "3":
            devolver_livro(dados, usuario)
        elif op == "4":
            historico(usuario, dados)
        elif op == "5":
            break
        else:
            print("Opção inválida.")

def menu_principal():
    dados = carregar_dados()

    while True:
        print("""
--- SISTEMA DE BIBLIOTECA ---
1. Registrar usuário
2. Login
3. Cadastrar livro (admin)
4. Sair
""")
        op = input("Opção: ")

        if op == "1":
            registrar_usuario(dados)
        elif op == "2":
            usuario = login(dados)
            if usuario:
                menu_usuario(usuario, dados)
        elif op == "3":
            cadastrar_livro(dados)
        elif op == "4":
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida.")

# ---------- EXECUÇÃO ----------

if __name__ == "__main__":
    menu_principal()
