import mysql.connector
from tkinter import messagebox
from .db_connection import conectar_bd

# Função para criar um novo projeto
def criar_projeto(nome, descricao, id_secretaria, data_inicio, data_fim):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projetos (nome, descricao, id_secretaria, data_inicio, data_fim) VALUES (%s, %s, %s, %s, %s)", (nome, descricao, id_secretaria, data_inicio, data_fim))
        conn.commit()
        conn.close()

# Função para alterar detalhes de um projeto
def alterar_projeto(id_projeto, nome, descricao, id_secretaria, data_inicio, data_fim):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE projetos SET nome=%s, descricao=%s, id_secretaria=%s, data_inicio=%s, data_fim=%s WHERE id_projeto=%s", (nome, descricao, id_secretaria, data_inicio, data_fim, id_projeto))
        conn.commit()
        conn.close()

# Função para excluir um projeto
def excluir_projeto(id_projeto):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM projetos WHERE id_projeto=%s", (id_projeto,))
        conn.commit()
        conn.close()

# Função para consultar projetos
def listar_projetos(filtro=None):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM projetos WHERE nome LIKE %s", (f'%{filtro}%',))
        else:
            cursor.execute("SELECT * FROM projetos")
        projetos = cursor.fetchall()
        conn.close()
        return projetos
    return [] 