import mysql.connector
from tkinter import messagebox
from .db_connection import conectar_bd

# Função para criar um novo evento
def criar_evento(nome, descricao, data_evento, id_secretaria, id_funcionario):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO eventos (nome, descricao, data_evento, id_secretaria, id_funcionario) VALUES (%s, %s, %s, %s, %s)", (nome, descricao, data_evento, id_secretaria, id_funcionario))
        conn.commit()
        conn.close()

# Função para atualizar informações de um evento
def atualizar_evento(id_evento, nome, descricao, data_evento):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE eventos SET nome=%s, descricao=%s, data_evento=%s WHERE id_evento=%s", (nome, descricao, data_evento, id_evento))
        conn.commit()
        conn.close()

# Função para cancelar ou excluir um evento
def excluir_evento(id_evento):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM eventos WHERE id_evento=%s", (id_evento,))
        conn.commit()
        conn.close()

# Função para listar eventos
def listar_eventos(filtro=None):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM eventos WHERE nome LIKE %s", (f'%{filtro}%',))
        else:
            cursor.execute("SELECT * FROM eventos")
        eventos = cursor.fetchall()
        conn.close()
        return eventos
    return [] 