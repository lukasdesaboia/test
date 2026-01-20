#python hospital.py
import json
import os
from datetime import datetime

ARQUIVO = "hospital.json"

# ---------- DADOS ----------

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "usuarios": {},
        "pacientes": {},
        "medicos": {},
        "consultas": []
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

# ---------- PACIENTES ----------

def cadastrar_paciente(dados):
    cpf = input("CPF do paciente: ")
    if cpf in dados["pacientes"]:
        print("Paciente já cadastrado.")
        return
    nome = input("Nome: ")
    idade = input("Idade: ")
    dados["pacientes"][cpf] = {
        "nome": nome,
        "idade": idade,
        "prontuario": []
    }
    salvar_dados(dados)
    print("Paciente cadastrado com sucesso!")

def listar_pacientes(dados):
    if not dados["pacientes"]:
        print("Nenhum paciente cadastrado.")
        return
    for cpf, p in dados["pacientes"].items():
        print(f"{cpf} - {p['nome']} ({p['idade']} anos)")

def adicionar_prontuario(dados):
    cpf = input("CPF do paciente: ")
    paciente = dados["pacientes"].get(cpf)
    if not paciente:
        print("Paciente não encontrado.")
        return
    anotacao = input("Anotação médica: ")
    paciente["prontuario"].append({
        "data": datetime.now().strftime("%d/%m/%Y"),
        "descricao": anotacao
    })
    salvar_dados(dados)
    print("Prontuário atualizado.")

# ---------- MÉDICOS ----------

def cadastrar_medico(dados):
    crm = input("CRM do médico: ")
    if crm in dados["medicos"]:
        print("Médico já cadastrado.")
        return
    nome = input("Nome do médico: ")
    especialidade = input("Especialidade: ")
    dados["medicos"][crm] = {
        "nome": nome,
        "especialidade": especialidade
    }
    salvar_dados(dados)
    print("Médico cadastrado com sucesso!")

def listar_medicos(dados):
    if not dados["medicos"]:
        print("Nenhum médico cadastrado.")
        return
    for crm, m in dados["medicos"].items():
        print(f"{crm} - Dr(a). {m['nome']} ({m['especialidade']})")

# ---------- CONSULTAS ----------

def agendar_consulta(dados):
    cpf = input("CPF do paciente: ")
    if cpf not in dados["pacientes"]:
        print("Paciente não encontrado.")
        return

    listar_medicos(dados)
    crm = input("CRM do médico: ")
    if crm not in dados["medicos"]:
        print("Médico não encontrado.")
        return

    data = input("Data da consulta (dd/mm/aaaa): ")

    dados["consultas"].append({
        "paciente": cpf,
        "medico": crm,
        "data": data
    })
    salvar_dados(dados)
    print("Consulta agendada com sucesso!")

def listar_consultas(dados):
    if not dados["consultas"]:
        print("Nenhuma consulta agendada.")
        return
    for c in dados["consultas"]:
        paciente = dados["pacientes"][c["paciente"]]["nome"]
        medico = dados["medicos"][c["medico"]]["nome"]
        print(f"{c['data']} - {paciente} com Dr(a). {medico}")

# ---------- MENUS ----------

def menu_sistema(dados):
    while True:
        print("""
--- SISTEMA HOSPITALAR ---
1. Cadastrar paciente
2. Listar pacientes
3. Cadastrar médico
4. Listar médicos
5. Agendar consulta
6. Listar consultas
7. Atualizar prontuário
8. Sair
""")
        op = input("Opção: ")

        if op == "1":
            cadastrar_paciente(dados)
        elif op == "2":
            listar_pacientes(dados)
        elif op == "3":
            cadastrar_medico(dados)
        elif op == "4":
            listar_medicos(dados)
        elif op == "5":
            agendar_consulta(dados)
        elif op == "6":
            listar_consultas(dados)
        elif op == "7":
            adicionar_prontuario(dados)
        elif op == "8":
            break
        else:
            print("Opção inválida.")

def sistema():
    dados = carregar_dados()

    while True:
        print("""
--- LOGIN HOSPITAL ---
1. Registrar usuário
2. Login
3. Sair
""")
        op = input("Opção: ")

        if op == "1":
            registrar_usuario(dados)
        elif op == "2":
            usuario = login(dados)
            if usuario:
                menu_sistema(dados)
        elif op == "3":
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida.")

# ---------- EXECUÇÃO ----------

if __name__ == "__main__":
    sistema()
