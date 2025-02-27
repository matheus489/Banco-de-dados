import mysql.connector
from tkinter import messagebox
from .db_connection import conectar_bd

# Funções para Funcionários_Projetos
def associar_funcionario_projeto(id_funcionario, id_projeto):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO funcionarios_projetos (id_funcionario, id_projeto) VALUES (%s, %s)", (id_funcionario, id_projeto))
        conn.commit()
        conn.close()


def remover_funcionario_projeto(id_funcionario, id_projeto):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM funcionarios_projetos WHERE id_funcionario=%s AND id_projeto=%s", (id_funcionario, id_projeto))
        conn.commit()
        conn.close()


def listar_funcionarios_por_projeto(id_projeto):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT f.id_funcionario, f.nome FROM funcionarios f JOIN funcionarios_projetos fp ON f.id_funcionario = fp.id_funcionario WHERE fp.id_projeto = %s", (id_projeto,))
        funcionarios = cursor.fetchall()
        conn.close()
        return funcionarios
    return []


def listar_projetos_por_funcionario(id_funcionario):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT p.id_projeto, p.nome FROM projetos p JOIN funcionarios_projetos fp ON p.id_projeto = fp.id_projeto WHERE fp.id_funcionario = %s", (id_funcionario,))
        projetos = cursor.fetchall()
        conn.close()
        return projetos
    return []

# Funções para Moradores_Eventos
def registrar_morador_evento(id_morador, id_evento):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO moradores_eventos (id_morador, id_evento) VALUES (%s, %s)", (id_morador, id_evento))
        conn.commit()
        conn.close()


def remover_morador_evento(id_morador, id_evento):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM moradores_eventos WHERE id_morador=%s AND id_evento=%s", (id_morador, id_evento))
        conn.commit()
        conn.close()


def listar_moradores_por_evento(id_evento):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT m.id_morador, m.nome FROM moradores m JOIN moradores_eventos me ON m.id_morador = me.id_morador WHERE me.id_evento = %s", (id_evento,))
        moradores = cursor.fetchall()
        conn.close()
        return moradores
    return []


def listar_eventos_por_morador(id_morador):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT e.id_evento, e.nome FROM eventos e JOIN moradores_eventos me ON e.id_evento = me.id_evento WHERE me.id_morador = %s", (id_morador,))
        eventos = cursor.fetchall()
        conn.close()
        return eventos
    return [] 