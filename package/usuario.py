# package/usuario.py

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
        self.pontos = 0

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def concluir_tarefa(self, nome_tarefa):
        for tarefa in self.tarefas:
            if tarefa.nome == nome_tarefa and not tarefa.concluida:
                tarefa.marcar_concluida()
                self.pontos += tarefa.pontos_ganhos()
                break

    def calcular_nivel(self):
        return self.pontos // 100

    def listar_tarefas(self, concluidas=False):
        return [t for t in self.tarefas if t.concluida == concluidas]

    def __str__(self):
        return f"{self.nome} - Nível: {self.calcular_nivel()} - Pontos: {self.pontos}"
