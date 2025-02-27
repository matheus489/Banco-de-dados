import mysql.connector
from tkinter import messagebox

# Configurações do banco de dados
db_config = {
    'user': 'root',
    'password': '#8611Beta',
    'host': '127.0.0.1',
    'database': 'db_2024_p5_t2'
}

# Função para conectar ao banco de dados
def conectar_bd():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
        return None

# Função para buscar dados de uma tabela
def buscar_dados(tabela):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela}")
        dados = cursor.fetchall()
        conn.close()
        return dados
    return []

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

# Função para criar um novo projeto
def criar_projeto(nome, descricao, id_secretaria):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projetos (nome, descricao, id_secretaria) VALUES (%s, %s, %s)", (nome, descricao, id_secretaria))
        conn.commit()
        conn.close()

# Função para alterar detalhes de um projeto
def alterar_projeto(id_projeto, nome, descricao, id_secretaria):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE projetos SET nome=%s, descricao=%s, id_secretaria=%s WHERE id_projeto=%s", (nome, descricao, id_secretaria, id_projeto))
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

# Função para registrar um novo morador
def registrar_morador(nome, endereco):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO moradores (nome, endereco) VALUES (%s, %s)", (nome, endereco))
        conn.commit()
        conn.close()

# Função para atualizar os dados de um morador
def atualizar_morador(id_morador, nome, endereco):
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE moradores SET nome=%s, endereco=%s WHERE id_morador=%s", (nome, endereco, id_morador))
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

def listar_relacionamentos():
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT me.id, m.nome AS morador_nome, e.nome AS evento_nome
            FROM moradores_eventos me
            JOIN moradores m ON me.id_morador = m.id_morador
            JOIN eventos e ON me.id_evento = e.id_evento
        """)
        relacionamentos = cursor.fetchall()
        conn.close()
        return relacionamentos
    return [] 