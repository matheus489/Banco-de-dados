import sys
import os
from tkinter import messagebox

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import Tk, Label, Button, StringVar, Entry, Toplevel, Frame, ttk, Text
from database.moradores import registrar_morador, atualizar_morador, excluir_morador, listar_moradores
from database.db_connection import (
    criar_secretaria, atualizar_secretaria, excluir_secretaria, listar_secretarias,
    associar_funcionario_projeto, remover_funcionario_projeto, listar_funcionarios_por_projeto, listar_projetos_por_funcionario,
    criar_evento, atualizar_evento, excluir_evento, listar_eventos,
    criar_projeto, excluir_projeto, listar_projetos,
    registrar_morador_evento, remover_morador_evento, listar_relacionamentos
)
from database.projetos import criar_projeto, alterar_projeto as atualizar_projeto, excluir_projeto
from database.reclamacoes import atualizar_reclamacao, remover_reclamacao as excluir_reclamacao, criar_reclamacao, listar_reclamacoes

class JanelaAdicionarSecretaria:
    def __init__(self, master, callback):
        self.janela = Toplevel(master)
        self.janela.title("Adicionar Secretaria")

        Label(self.janela, text="Nome:").pack()
        self.nome = Entry(self.janela)
        self.nome.pack()

        Label(self.janela, text="Descrição:").pack()
        self.descricao = Entry(self.janela)
        self.descricao.pack()

        Label(self.janela, text="Localização:").pack()
        self.localizacao = Entry(self.janela)
        self.localizacao.pack()

        Button(self.janela, text="Adicionar", command=self.adicionar).pack()
        self.callback = callback

    def adicionar(self):
        criar_secretaria(self.nome.get(), self.descricao.get(), self.localizacao.get())
        exibir_alerta("Secretaria adicionada com sucesso!")
        self.callback()
        self.janela.destroy()

class JanelaAtualizarSecretaria:
    def __init__(self, master, callback):
        self.janela = Toplevel(master)
        self.janela.title("Atualizar Secretaria")

        Label(self.janela, text="ID:").pack()
        self.id_secretaria = Entry(self.janela)
        self.id_secretaria.pack()

        Label(self.janela, text="Nome:").pack()
        self.nome = Entry(self.janela)
        self.nome.pack()

        Label(self.janela, text="Descrição:").pack()
        self.descricao = Entry(self.janela)
        self.descricao.pack()

        Label(self.janela, text="Localização:").pack()
        self.localizacao = Entry(self.janela)
        self.localizacao.pack()

        Button(self.janela, text="Atualizar", command=self.atualizar).pack()
        self.callback = callback

    def atualizar(self):
        atualizar_secretaria(self.id_secretaria.get(), self.nome.get(), self.descricao.get(), self.localizacao.get())
        exibir_alerta("Secretaria atualizada com sucesso!")
        self.callback()
        self.janela.destroy()

class JanelaExcluirSecretaria:
    def __init__(self, master, callback):
        self.janela = Toplevel(master)
        self.janela.title("Excluir Secretaria")

        Label(self.janela, text="ID:").pack()
        self.id_secretaria = Entry(self.janela)
        self.id_secretaria.pack()

        Button(self.janela, text="Excluir", command=self.excluir).pack()
        self.callback = callback

    def excluir(self):
        excluir_secretaria(self.id_secretaria.get())
        exibir_alerta("Secretaria excluída com sucesso!")
        self.callback()
        self.janela.destroy()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão")

        self.resultado = StringVar()

        # Criar o Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Criar frames para cada aba
        self.frame_secretarias = Frame(self.notebook)
        self.frame_funcionarios_projetos = Frame(self.notebook)
        self.frame_eventos = Frame(self.notebook)
        self.frame_moradores = Frame(self.notebook)
        self.frame_projetos = Frame(self.notebook)
        self.frame_reclamacoes = Frame(self.notebook)
        self.frame_relacionamentos = Frame(self.notebook)

        # Adicionar frames ao Notebook
        self.notebook.add(self.frame_secretarias, text="Secretarias")
        self.notebook.add(self.frame_funcionarios_projetos, text="Funcionários e Projetos")
        self.notebook.add(self.frame_eventos, text="Eventos")
        self.notebook.add(self.frame_moradores, text="Moradores")
        self.notebook.add(self.frame_projetos, text="Projetos")
        self.notebook.add(self.frame_reclamacoes, text="Reclamações")
        self.notebook.add(self.frame_relacionamentos, text="Relacionamentos")

        # Adicionar widgets ao frame de Secretarias
        Button(self.frame_secretarias, text="Adicionar Secretaria", command=self.janela_adicionar_secretaria).pack()
        Button(self.frame_secretarias, text="Atualizar Secretaria", command=self.janela_atualizar_secretaria).pack()
        Button(self.frame_secretarias, text="Excluir Secretaria", command=self.janela_excluir_secretaria).pack()
        Button(self.frame_secretarias, text="Listar Secretarias", command=self.mostrar_secretarias).pack()

        # Adicionar widgets ao frame de Funcionários e Projetos
        Button(self.frame_funcionarios_projetos, text="Associar Funcionário a Projeto", command=self.janela_associar_funcionario_projeto).pack()
        Button(self.frame_funcionarios_projetos, text="Remover Funcionário de Projeto", command=self.janela_remover_funcionario_projeto).pack()
        Button(self.frame_funcionarios_projetos, text="Listar Funcionários por Projeto", command=self.janela_listar_funcionarios_por_projeto).pack()
        Button(self.frame_funcionarios_projetos, text="Listar Projetos por Funcionário", command=self.listar_projetos).pack()

        # Adicionar widgets ao frame de Eventos
        Button(self.frame_eventos, text="Criar Evento", command=self.janela_criar_evento).pack()
        Button(self.frame_eventos, text="Atualizar Evento", command=self.janela_atualizar_evento).pack()
        Button(self.frame_eventos, text="Excluir Evento", command=self.janela_excluir_evento).pack()
        Button(self.frame_eventos, text="Listar Eventos", command=self.listar_eventos).pack()

        # Adicionar widgets ao frame de Moradores
        Button(self.frame_moradores, text="Registrar Morador", command=self.janela_registrar_morador).pack()
        Button(self.frame_moradores, text="Atualizar Morador", command=self.janela_atualizar_morador).pack()
        Button(self.frame_moradores, text="Excluir Morador", command=self.janela_excluir_morador).pack()
        Button(self.frame_moradores, text="Listar Moradores", command=self.listar_moradores).pack()

        # Adicionar widgets ao frame de Projetos
        Button(self.frame_projetos, text="Criar Projeto", command=self.janela_criar_projeto).pack()
        Button(self.frame_projetos, text="Atualizar Projeto", command=self.janela_atualizar_projeto).pack()
        Button(self.frame_projetos, text="Excluir Projeto", command=self.janela_excluir_projeto).pack()

        # Adicionar widgets ao frame de Reclamações
        Button(self.frame_reclamacoes, text="Criar Reclamação", command=self.janela_criar_reclamacao).pack()
        Button(self.frame_reclamacoes, text="Atualizar Reclamação", command=self.janela_atualizar_reclamacao).pack()
        Button(self.frame_reclamacoes, text="Excluir Reclamação", command=self.janela_excluir_reclamacao).pack()
        Button(self.frame_reclamacoes, text="Listar Reclamações", command=self.listar_reclamacoes).pack()

        # Adicionar widgets ao frame de Relacionamentos
        Button(self.frame_relacionamentos, text="Associar Morador a Evento", command=self.janela_associar_morador_evento).pack()
        Button(self.frame_relacionamentos, text="Remover Morador de Evento", command=self.janela_remover_morador_evento).pack()
        Button(self.frame_relacionamentos, text="Listar Relacionamentos", command=self.listar_relacionamentos).pack()

        Label(self.frame_funcionarios_projetos, textvariable=self.resultado).pack()

    def janela_adicionar_secretaria(self):
        JanelaAdicionarSecretaria(self.root, self.mostrar_secretarias)

    def janela_atualizar_secretaria(self):
        JanelaAtualizarSecretaria(self.root, self.mostrar_secretarias)

    def janela_excluir_secretaria(self):
        JanelaExcluirSecretaria(self.root, self.mostrar_secretarias)

    def janela_associar_funcionario_projeto(self):
        janela = Toplevel(self.root)
        janela.title("Associar Funcionário a Projeto")

        Label(janela, text="ID Funcionário:").pack()
        id_funcionario = Entry(janela)
        id_funcionario.pack()

        Label(janela, text="ID Projeto:").pack()
        id_projeto = Entry(janela)
        id_projeto.pack()

        Button(janela, text="Associar", command=lambda: self.associar_funcionario_projeto(id_funcionario.get(), id_projeto.get())).pack()

    def associar_funcionario_projeto(self, id_funcionario, id_projeto):
        associar_funcionario_projeto(id_funcionario, id_projeto)
        exibir_alerta("Funcionário associado ao projeto com sucesso!")

    def janela_remover_funcionario_projeto(self):
        janela = Toplevel(self.root)
        janela.title("Remover Funcionário de Projeto")

        Label(janela, text="ID Funcionário:").pack()
        id_funcionario = Entry(janela)
        id_funcionario.pack()

        Label(janela, text="ID Projeto:").pack()
        id_projeto = Entry(janela)
        id_projeto.pack()

        Button(janela, text="Remover", command=lambda: self.remover_funcionario_projeto(id_funcionario.get(), id_projeto.get())).pack()

    def remover_funcionario_projeto(self, id_funcionario, id_projeto):
        remover_funcionario_projeto(id_funcionario, id_projeto)
        exibir_alerta("Funcionário removido do projeto com sucesso!")

    def janela_listar_funcionarios_por_projeto(self):
        janela = Toplevel(self.root)
        janela.title("Listar Funcionários por Projeto")

        Label(janela, text="ID Projeto:").pack()
        id_projeto = Entry(janela)
        id_projeto.pack()

        Button(janela, text="Listar", command=lambda: self.listar_funcionarios_por_projeto(id_projeto.get())).pack()

    def listar_funcionarios_por_projeto(self, id_projeto):
        funcionarios = listar_funcionarios_por_projeto(id_projeto)
        if funcionarios:
            self.exibir_resultados_em_janela("Funcionários por Projeto", funcionarios)
        else:
            exibir_alerta("Nenhum funcionário encontrado para este projeto.")

    def mostrar_secretarias(self):
        secretarias = listar_secretarias()
        if secretarias:
            self.exibir_resultados_em_janela("Secretarias", secretarias)
        else:
            exibir_alerta("Nenhuma secretaria encontrada.")

    # Funções para Eventos
    def janela_criar_evento(self):
        janela = Toplevel(self.root)
        janela.title("Criar Evento")
        
        Label(janela, text="Nome:").pack()
        nome = Entry(janela)
        nome.pack()
        
        Label(janela, text="Descrição:").pack()
        descricao = Entry(janela)
        descricao.pack()
        
        Label(janela, text="Data do Evento (YYYY-MM-DD):").pack()
        data_evento = Entry(janela)
        data_evento.pack()
        
        Label(janela, text="ID Secretaria:").pack()
        id_secretaria = Entry(janela)
        id_secretaria.pack()
        
        Label(janela, text="ID Funcionário:").pack()
        id_funcionario = Entry(janela)
        id_funcionario.pack()
        
        Button(janela, text="Criar", command=lambda: criar_evento(nome.get(), descricao.get(), data_evento.get(), id_secretaria.get(), id_funcionario.get())).pack()

    def janela_atualizar_evento(self):
        janela = Toplevel(self.root)
        janela.title("Atualizar Evento")
        
        Label(janela, text="ID Evento:").pack()
        id_evento = Entry(janela)
        id_evento.pack()
        
        Label(janela, text="Nome:").pack()
        nome = Entry(janela)
        nome.pack()
        
        Label(janela, text="Descrição:").pack()
        descricao = Entry(janela)
        descricao.pack()
        
        Label(janela, text="Data do Evento (YYYY-MM-DD):").pack()
        data_evento = Entry(janela)
        data_evento.pack()
        
        Label(janela, text="ID Secretaria:").pack()
        id_secretaria = Entry(janela)
        id_secretaria.pack()
        
        Label(janela, text="ID Funcionário:").pack()
        id_funcionario = Entry(janela)
        id_funcionario.pack()
        
        Button(janela, text="Atualizar", command=lambda: self.atualizar_evento(id_evento.get(), nome.get(), descricao.get(), data_evento.get())).pack()

    def atualizar_evento(self, id_evento, nome, descricao, data_evento):
        atualizar_evento(id_evento, nome, descricao, data_evento)
        exibir_alerta("Evento atualizado com sucesso!")

    def janela_excluir_evento(self):
        janela = Toplevel(self.root)
        janela.title("Excluir Evento")
        
        Label(janela, text="ID Evento:").pack()
        id_evento = Entry(janela)
        id_evento.pack()
        
        Button(janela, text="Excluir", command=lambda: self.excluir_evento(id_evento.get())).pack()

    def excluir_evento(self, id_evento):
        excluir_evento(id_evento)
        exibir_alerta("Evento excluído com sucesso!")

    # Funções para Moradores
    def janela_registrar_morador(self):
        janela = Toplevel(self.root)
        janela.title("Registrar Morador")
        
        Label(janela, text="Nome:").pack()
        nome = Entry(janela)
        nome.pack()
        
        Label(janela, text="Endereço:").pack()
        endereco = Entry(janela)
        endereco.pack()
        
        Label(janela, text="Idade:").pack()
        idade = Entry(janela)
        idade.pack()
        
        Button(janela, text="Registrar", command=lambda: registrar_morador(nome.get(), endereco.get(), idade.get())).pack()

    def janela_atualizar_morador(self):
        janela = Toplevel(self.root)
        janela.title("Atualizar Morador")
        
        Label(janela, text="ID Morador:").pack()
        id_morador = Entry(janela)
        id_morador.pack()
        
        Label(janela, text="Nome:").pack()
        nome = Entry(janela)
        nome.pack()
        
        Label(janela, text="Endereço:").pack()
        endereco = Entry(janela)
        endereco.pack()
        
        Label(janela, text="Idade:").pack()
        idade = Entry(janela)
        idade.pack()
        
        Button(janela, text="Atualizar", command=lambda: self.atualizar_morador(id_morador.get(), nome.get(), endereco.get(), idade.get())).pack()

    def atualizar_morador(self, id_morador, nome, endereco, idade):
        atualizar_morador(id_morador, nome, endereco, idade)
        exibir_alerta("Morador atualizado com sucesso!")

    def janela_excluir_morador(self):
        janela = Toplevel(self.root)
        janela.title("Excluir Morador")
        
        Label(janela, text="ID Morador:").pack()
        id_morador = Entry(janela)
        id_morador.pack()
        
        Button(janela, text="Excluir", command=lambda: self.excluir_morador(id_morador.get())).pack()

    def excluir_morador(self, id_morador):
        excluir_morador(id_morador)
        exibir_alerta("Morador excluído com sucesso!")

    # Funções para Projetos
    def janela_criar_projeto(self):
        janela = Toplevel(self.root)
        janela.title("Criar Projeto")
        
        Label(janela, text="Nome:").pack()
        nome = Entry(janela)
        nome.pack()
        
        Label(janela, text="Descrição:").pack()
        descricao = Entry(janela)
        descricao.pack()
        
        Label(janela, text="ID Secretaria:").pack()
        id_secretaria = Entry(janela)
        id_secretaria.pack()
        
        Label(janela, text="Data Início (YYYY-MM-DD):").pack()
        data_inicio = Entry(janela)
        data_inicio.pack()
        
        Label(janela, text="Data Fim (YYYY-MM-DD):").pack()
        data_fim = Entry(janela)
        data_fim.pack()
        
        Button(janela, text="Criar", command=lambda: criar_projeto(nome.get(), descricao.get(), id_secretaria.get(), data_inicio.get(), data_fim.get())).pack()

    def janela_atualizar_projeto(self):
        janela = Toplevel(self.root)
        janela.title("Atualizar Projeto")
        
        Label(janela, text="ID Projeto:").pack()
        id_projeto = Entry(janela)
        id_projeto.pack()
        
        Label(janela, text="Nome:").pack()
        nome = Entry(janela)
        nome.pack()
        
        Label(janela, text="Descrição:").pack()
        descricao = Entry(janela)
        descricao.pack()
        
        Label(janela, text="ID Secretaria:").pack()
        id_secretaria = Entry(janela)
        id_secretaria.pack()
        
        Label(janela, text="Data Início (YYYY-MM-DD):").pack()
        data_inicio = Entry(janela)
        data_inicio.pack()
        
        Label(janela, text="Data Fim (YYYY-MM-DD):").pack()
        data_fim = Entry(janela)
        data_fim.pack()
        
        Button(janela, text="Atualizar", command=lambda: self.atualizar_projeto(id_projeto.get(), nome.get(), descricao.get(), id_secretaria.get(), data_inicio.get(), data_fim.get())).pack()

    def atualizar_projeto(self, id_projeto, nome, descricao, id_secretaria, data_inicio, data_fim):
        atualizar_projeto(id_projeto, nome, descricao, id_secretaria, data_inicio, data_fim)
        exibir_alerta("Projeto atualizado com sucesso!")

    def janela_excluir_projeto(self):
        janela = Toplevel(self.root)
        janela.title("Excluir Projeto")
        
        Label(janela, text="ID Projeto:").pack()
        id_projeto = Entry(janela)
        id_projeto.pack()
        
        Button(janela, text="Excluir", command=lambda: self.excluir_projeto(id_projeto.get())).pack()

    def excluir_projeto(self, id_projeto):
        excluir_projeto(id_projeto)
        exibir_alerta("Projeto excluído com sucesso!")

    # Funções para Reclamações
    def janela_criar_reclamacao(self):
        janela = Toplevel(self.root)
        janela.title("Criar Reclamação")
        
        Label(janela, text="Descrição:").pack()
        descricao = Entry(janela)
        descricao.pack()
        
        Label(janela, text="Data (YYYY-MM-DD):").pack()
        data = Entry(janela)
        data.pack()
        
        Label(janela, text="ID Morador:").pack()
        id_morador = Entry(janela)
        id_morador.pack()
        
        Label(janela, text="ID Secretaria:").pack()
        id_secretaria = Entry(janela)
        id_secretaria.pack()
        
        Label(janela, text="ID Funcionário:").pack()
        id_funcionario = Entry(janela)
        id_funcionario.pack()
        
        Button(janela, text="Criar", command=lambda: criar_reclamacao(descricao.get(), data.get(), id_morador.get(), id_secretaria.get(), id_funcionario.get())).pack()

    def janela_atualizar_reclamacao(self):
        janela = Toplevel(self.root)
        janela.title("Atualizar Reclamação")
        
        Label(janela, text="ID Reclamação:").pack()
        id_reclamacao = Entry(janela)
        id_reclamacao.pack()
        
        Label(janela, text="Descrição:").pack()
        descricao = Entry(janela)
        descricao.pack()
        
        Label(janela, text="Data (YYYY-MM-DD):").pack()
        data = Entry(janela)
        data.pack()
        
        Button(janela, text="Atualizar", command=lambda: self.atualizar_reclamacao(id_reclamacao.get(), descricao.get(), data.get())).pack()

    def atualizar_reclamacao(self, id_reclamacao, descricao, data):
        atualizar_reclamacao(id_reclamacao, descricao, data)
        exibir_alerta("Reclamação atualizada com sucesso!")

    def janela_excluir_reclamacao(self):
        janela = Toplevel(self.root)
        janela.title("Excluir Reclamação")
        
        Label(janela, text="ID Reclamação:").pack()
        id_reclamacao = Entry(janela)
        id_reclamacao.pack()
        
        Button(janela, text="Excluir", command=lambda: excluir_reclamacao(id_reclamacao.get())).pack()

    def excluir_reclamacao(self, id_reclamacao):
        excluir_reclamacao(id_reclamacao)
        exibir_alerta("Reclamação excluída com sucesso!")

    # Funções para Relacionamentos
    def janela_associar_morador_evento(self):
        janela = Toplevel(self.root)
        janela.title("Associar Morador a Evento")
        
        Label(janela, text="ID Morador:").pack()
        id_morador = Entry(janela)
        id_morador.pack()
        
        Label(janela, text="ID Evento:").pack()
        id_evento = Entry(janela)
        id_evento.pack()
        
        Button(janela, text="Associar", command=lambda: self.associar_morador_evento(id_morador.get(), id_evento.get())).pack()

    def associar_morador_evento(self, id_morador, id_evento):
        registrar_morador_evento(id_morador, id_evento)
        exibir_alerta("Morador associado ao evento com sucesso!")

    def janela_remover_morador_evento(self):
        janela = Toplevel(self.root)
        janela.title("Remover Morador de Evento")
        
        Label(janela, text="ID Morador:").pack()
        id_morador = Entry(janela)
        id_morador.pack()
        
        Label(janela, text="ID Evento:").pack()
        id_evento = Entry(janela)
        id_evento.pack()
        
        Button(janela, text="Remover", command=lambda: self.remover_morador_evento(id_morador.get(), id_evento.get())).pack()

    def remover_morador_evento(self, id_morador, id_evento):
        remover_morador_evento(id_morador, id_evento)
        exibir_alerta("Morador removido do evento com sucesso!")

    def listar_eventos(self):
        eventos = listar_eventos()
        if eventos:
            self.exibir_resultados_em_janela("Eventos", eventos)
        else:
            exibir_alerta("Nenhum evento encontrado.")

    def listar_moradores(self):
        moradores = listar_moradores()
        if moradores:
            self.exibir_resultados_em_janela("Moradores", moradores)
        else:
            exibir_alerta("Nenhum morador encontrado.")

    def listar_projetos(self):
        projetos = listar_projetos()
        if projetos:
            self.exibir_resultados_em_janela("Projetos", projetos)
        else:
            exibir_alerta("Nenhum projeto encontrado.")

    def listar_reclamacoes(self):
        reclamacoes = listar_reclamacoes()
        if reclamacoes:
            self.exibir_resultados_em_janela("Reclamações", reclamacoes)
        else:
            exibir_alerta("Nenhuma reclamação encontrada.")

    def listar_relacionamentos(self):
        relacionamentos = listar_relacionamentos()
        if relacionamentos:
            self.exibir_resultados_em_janela("Relacionamentos", relacionamentos)
        else:
            exibir_alerta("Nenhum relacionamento encontrado.")

    def exibir_resultados_em_janela(self, titulo, dados):
        janela = Toplevel(self.root)
        janela.title(titulo)
        text_area = Text(janela, wrap='word')
        text_area.pack(expand=True, fill='both')
        for linha in dados:
            text_area.insert('end', f"{linha}\n")
        text_area.config(state='disabled')

# Função de utilidade para exibir alertas
def exibir_alerta(mensagem):
    messagebox.showinfo("Operação Concluída", mensagem)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop() 