import mysql.connector
from tkinter import messagebox
from .db_connection import conectar_bd

# Função para registrar um novo morador
def registrar_morador(nome, endereco, idade):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO moradores (nome, endereco, idade) VALUES (%s, %s, %s)", (nome, endereco, idade))
        conn.commit()
        conn.close()

# Função para atualizar os dados de um morador
def atualizar_morador(id_morador, nome, endereco, idade):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE moradores SET nome=%s, endereco=%s, idade=%s WHERE id_morador=%s", (nome, endereco, idade, id_morador))
        conn.commit()
        conn.close()

# Função para excluir o cadastro de um morador
def excluir_morador(id_morador):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM moradores WHERE id_morador=%s", (id_morador,))
        conn.commit()
        conn.close()

# Função para listar moradores
def listar_moradores(filtro=None):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM moradores WHERE nome LIKE %s OR endereco LIKE %s", (f'%{filtro}%', f'%{filtro}%'))
        else:
            cursor.execute("SELECT * FROM moradores")
        moradores = cursor.fetchall()
        conn.close()
        return moradores
    return [] 