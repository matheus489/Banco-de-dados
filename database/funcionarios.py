import mysql.connector
from tkinter import messagebox
from .db_connection import conectar_bd

# Função para adicionar um novo funcionário
def adicionar_funcionario(nome, cargo, id_secretaria):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO funcionarios (nome, cargo, id_secretaria) VALUES (%s, %s, %s)", (nome, cargo, id_secretaria))
        conn.commit()
        conn.close()

# Função para atualizar informações de um funcionário
def atualizar_funcionario(id_funcionario, nome, cargo, id_secretaria):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE funcionarios SET nome=%s, cargo=%s, id_secretaria=%s WHERE id_funcionario=%s", (nome, cargo, id_secretaria, id_funcionario))
        conn.commit()
        conn.close()

# Função para remover um funcionário
def remover_funcionario(id_funcionario):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE id_funcionario=%s", (id_funcionario,))
        conn.commit()
        conn.close()

# Função para listar funcionários
def listar_funcionarios(filtro=None):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM funcionarios WHERE nome LIKE %s OR cargo LIKE %s", (f'%{filtro}%', f'%{filtro}%'))
        else:
            cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()
        conn.close()
        return funcionarios
    return [] 