from .usuario import Usuario
from .tarefa import Tarefa, TarefaUrgente
from .mixins import SerializableMixin
import os

class Sistema(SerializableMixin):
    def __init__(self):
        self.usuario = None
        self.db_path = 'usuario.db'

    def iniciar(self):
        print("Bem-vindo ao Gerenciador de Tarefas com Gamificação!")
        if os.path.exists(self.db_path):
            self.usuario = self.carregar(self.db_path)
            print(f"Usuário carregado: {self.usuario.nome}")
        else:
            nome = input("Digite seu nome: ")
            self.usuario = Usuario(nome)

        while True:
            self.menu()
            self.salvar(self.db_path)

    def menu(self):
        print("\n1. Adicionar tarefa")
        print("2. Concluir tarefa")
        print("3. Listar tarefas pendentes")
        print("4. Listar tarefas concluídas")
        print("5. Ver status do usuário")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            self.adicionar_tarefa()
        elif escolha == '2':
            self.concluir_tarefa()
        elif escolha == '3':
            self.listar_tarefas(False)
        elif escolha == '4':
            self.listar_tarefas(True)
        elif escolha == '5':
            print(self.usuario)
        elif escolha == '6':
            print("Saindo...")
            exit()
        else:
            print("Opção inválida!")

    def adicionar_tarefa(self):
        nome = input("Nome da tarefa: ")
        descricao = input("Descrição: ")
        prioridade = input("Prioridade (baixa, média, alta): ")
        prazo = input("Prazo (dd/mm/aaaa): ")
        urgente = input("É uma tarefa urgente? (s/n): ")
        if urgente.lower() == 's':
            tarefa = TarefaUrgente(nome, descricao, prioridade, prazo)
        else:
            tarefa = Tarefa(nome, descricao, prioridade, prazo)
        self.usuario.adicionar_tarefa(tarefa)

    def concluir_tarefa(self):
        nome = input("Nome da tarefa a concluir: ")
        self.usuario.concluir_tarefa(nome)

    def listar_tarefas(self, concluidas):
        tarefas = self.usuario.listar_tarefas(concluidas)
        if not tarefas:
            print("Nenhuma tarefa encontrada.")
        for t in tarefas:
            print(t)
