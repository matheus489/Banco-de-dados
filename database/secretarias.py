import mysql.connector
from tkinter import messagebox
from .db_connection import conectar_bd

# Função para criar uma nova secretaria
def criar_secretaria(nome, descricao, localizacao):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO secretarias (nome, descricao, localizacao) VALUES (%s, %s, %s)", (nome, descricao, localizacao))
        conn.commit()
        conn.close()

# Função para atualizar uma secretaria existente
def atualizar_secretaria(id_secretaria, nome, descricao, localizacao):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE secretarias SET nome=%s, descricao=%s, localizacao=%s WHERE id_secretaria=%s", (nome, descricao, localizacao, id_secretaria))
        conn.commit()
        conn.close()

# Função para excluir uma secretaria
def excluir_secretaria(id_secretaria):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM secretarias WHERE id_secretaria=%s", (id_secretaria,))
        conn.commit()
        conn.close()

# Função para consultar ou listar secretarias
def listar_secretarias(filtro=None):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM secretarias WHERE nome LIKE %s OR localizacao LIKE %s", (f'%{filtro}%', f'%{filtro}%'))
        else:
            cursor.execute("SELECT * FROM secretarias")
        secretarias = cursor.fetchall()
        conn.close()
        return secretarias
    return [] 