#python hospital_db.py
import sqlite3
from datetime import datetime

# ---------- CONEXÃO ----------

def conectar():
    return sqlite3.connect("hospital.db")

# ---------- CRIAÇÃO DAS TABELAS ----------

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        senha TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        cpf TEXT PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
        crm TEXT PRIMARY KEY,
        nome TEXT,
        especialidade TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_paciente TEXT,
        crm_medico TEXT,
        data TEXT,
        FOREIGN KEY (cpf_paciente) REFERENCES pacientes(cpf),
        FOREIGN KEY (crm_medico) REFERENCES medicos(crm)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prontuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_paciente TEXT,
        data TEXT,
        descricao TEXT,
        FOREIGN KEY (cpf_paciente) REFERENCES pacientes(cpf)
    )
    """)

    conn.commit()
    conn.close()

# ---------- USUÁRIOS ----------

def registrar_usuario():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO usuarios VALUES (NULL, ?, ?)", (usuario, senha))
        conn.commit()
        print("Usuário registrado!")
    except:
        print("Usuário já existe.")
    conn.close()

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print(f"Bem-vindo, {usuario}!")
        return True
    print("Login inválido.")
    return False

# ---------- PACIENTES ----------

def cadastrar_paciente():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = input("Idade: ")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO pacientes VALUES (?, ?, ?)", (cpf, nome, idade))
        conn.commit()
        print("Paciente cadastrado!")
    except:
        print("Paciente já existe.")
    conn.close()

def listar_pacientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")
    for p in cursor.fetchall():
        print(f"{p[0]} - {p[1]} ({p[2]} anos)")
    conn.close()

# ---------- MÉDICOS ----------

def cadastrar_medico():
    crm = input("CRM: ")
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO medicos VALUES (?, ?, ?)", (crm, nome, especialidade))
        conn.commit()
        print("Médico cadastrado!")
    except:
        print("Médico já existe.")
    conn.close()

def listar_medicos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicos")
    for m in cursor.fetchall():
        print(f"{m[0]} - Dr(a). {m[1]} ({m[2]})")
    conn.close()

# ---------- CONSULTAS ----------

def agendar_consulta():
    cpf = input("CPF do paciente: ")
    crm = input("CRM do médico: ")
    data = input("Data (dd/mm/aaaa): ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO consultas VALUES (NULL, ?, ?, ?)",
        (cpf, crm, data)
    )
    conn.commit()
    conn.close()
    print("Consulta agendada!")

def listar_consultas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT consultas.data, pacientes.nome, medicos.nome
    FROM consultas
    JOIN pacientes ON consultas.cpf_paciente = pacientes.cpf
    JOIN medicos ON consultas.crm_medico = medicos.crm
    """)

    for c in cursor.fetchall():
        print(f"{c[0]} - {c[1]} com Dr(a). {c[2]}")
    conn.close()

# ---------- PRONTUÁRIO ----------

def adicionar_prontuario():
    cpf = input("CPF do paciente: ")
    descricao = input("Descrição médica: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO prontuarios VALUES (NULL, ?, ?, ?)",
        (cpf, datetime.now().strftime("%d/%m/%Y"), descricao)
    )
    conn.commit()
    conn.close()
    print("Prontuário atualizado!")

# ---------- MENU ----------

def menu():
    criar_tabelas()

    if not login():
        return

    while True:
        print("""
--- SISTEMA HOSPITALAR (BANCO DE DADOS) ---
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
            cadastrar_paciente()
        elif op == "2":
            listar_pacientes()
        elif op == "3":
            cadastrar_medico()
        elif op == "4":
            listar_medicos()
        elif op == "5":
            agendar_consulta()
        elif op == "6":
            listar_consultas()
        elif op == "7":
            adicionar_prontuario()
        elif op == "8":
            break
        else:
            print("Opção inválida.")

# ---------- EXECUÇÃO ----------

if __name__ == "__main__":
    criar_tabelas()
    registrar_usuario()
    menu()
