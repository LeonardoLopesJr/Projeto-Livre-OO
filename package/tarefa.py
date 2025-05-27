# package/tarefa.py
from datetime import datetime

class Tarefa:
    def __init__(self, nome, descricao, prioridade, prazo):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = 'Concluída' if self.concluida else 'Pendente'
        return f"{self.nome} - {status} - Prioridade: {self.prioridade} - Prazo: {self.prazo}"

    def pontos_ganhos(self):
        return 10  # padrão para tarefa comum

class TarefaUrgente(Tarefa):
    def pontos_ganhos(self):
        return