import mysql.connector
from tkinter import messagebox
from .db_connection import conectar_bd

# Função para criar uma nova reclamação
def criar_reclamacao(descricao, data, id_morador, id_secretaria, id_funcionario):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reclamacoes (descricao, data, id_morador, id_secretaria, id_funcionario) VALUES (%s, %s, %s, %s, %s)", (descricao, data, id_morador, id_secretaria, id_funcionario))
        conn.commit()
        conn.close()

# Função para atualizar uma reclamação
def atualizar_reclamacao(id_reclamacao, descricao, data):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE reclamacoes SET descricao=%s, data=%s WHERE id_reclamacao=%s", (descricao, data, id_reclamacao))
        conn.commit()
        conn.close()

# Função para remover uma reclamação
def remover_reclamacao(id_reclamacao):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reclamacoes WHERE id_reclamacao=%s", (id_reclamacao,))
        conn.commit()
        conn.close()

# Função para consultar reclamações
def listar_reclamacoes(filtro=None):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM reclamacoes WHERE descricao LIKE %s", (f'%{filtro}%',))
        else:
            cursor.execute("SELECT * FROM reclamacoes")
        reclamacoes = cursor.fetchall()
        conn.close()
        return reclamacoes
    return [] 