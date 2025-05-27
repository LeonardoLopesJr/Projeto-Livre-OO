import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from package.tarefa import Tarefa, TarefaUrgente
from package.usuario import Usuario


class App:
    def __init__(self, root):
        self.usuario = Usuario("Jogador")
        self.root = root
        self.root.title("🎮 Gerenciador de Tarefas com Gamificação")
        self.root.configure(bg="#eaf6ff")  # Fundo claro azul

        # Estilos
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TButton",
                        font=("Segoe UI", 10),
                        padding=6,
                        foreground="#ffffff",
                        background="#2980b9")
        style.map("TButton",
                  background=[("active", "#3498db")])

        style.configure("TLabel", font=("Segoe UI", 10), background="#eaf6ff")
        style.configure("Header.TLabel",
                        font=("Segoe UI", 16, "bold"),
                        background="#eaf6ff",
                        foreground="#2c3e50")

        # Título
        ttk.Label(root, text="📋 Gerenciador de Tarefas", style="Header.TLabel").pack(pady=10)

        # Formulário de entrada
        form_frame = ttk.Frame(root)
        form_frame.pack(padx=20, pady=10)

        self.nome_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.prazo_var = tk.StringVar()
        self.prioridade_var = tk.StringVar()

        self._add_labeled_entry(form_frame, "📝 Nome:", self.nome_var, 0)
        self._add_labeled_entry(form_frame, "📄 Descrição:", self.desc_var, 1)
        self._add_labeled_entry(form_frame, "📆 Prazo:", self.prazo_var, 2)
        self._add_labeled_entry(form_frame, "⚠️ Prioridade:", self.prioridade_var, 3)

        # Botões
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="➕ Adicionar", command=self.adicionar_tarefa).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="✅ Concluir", command=self.concluir_tarefa).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="📋 Ver Tarefas", command=self.listar_tarefas).grid(row=0, column=2, padx=5)
        ttk.Button(btn_frame, text="👤 Status", command=self.mostrar_status).grid(row=0, column=3, padx=5)

        # Área de saída com rolagem
        output_frame = ttk.Frame(root)
        output_frame.pack(padx=20, pady=10)

        self.resultado = tk.Text(output_frame, height=12, width=70,
                                 bg="#ffffff", fg="#2c3e50", font=("Consolas", 10), relief=tk.FLAT, bd=1)
        self.resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(output_frame, command=self.resultado.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.resultado.config(yscrollcommand=scrollbar.set)

    def _add_labeled_entry(self, frame, label, var, row):
        ttk.Label(frame, text=label).grid(row=row, column=0, sticky="e", padx=5, pady=3)
        ttk.Entry(frame, textvariable=var, width=40).grid(row=row, column=1, padx=5, pady=3)

    def adicionar_tarefa(self):
        nome = self.nome_var.get()
        desc = self.desc_var.get()
        prazo = self.prazo_var.get()
        prioridade = self.prioridade_var.get().lower()

        if not nome:
            messagebox.showwarning("Atenção", "O nome da tarefa é obrigatório.")
            return

        if prioridade == "urgente":
            tarefa = TarefaUrgente(nome, desc, prioridade, prazo)
        else:
            tarefa = Tarefa(nome, desc, prioridade, prazo)

        self.usuario.adicionar_tarefa(tarefa)
        messagebox.showinfo("Sucesso", "Tarefa adicionada!")

        self.nome_var.set("")
        self.desc_var.set("")
        self.prazo_var.set("")
        self.prioridade_var.set("")

    def concluir_tarefa(self):
        nome = simpledialog.askstring("Concluir Tarefa", "Nome da tarefa a concluir:")
        if nome:
            self.usuario.concluir_tarefa(nome)
            messagebox.showinfo("Concluído", "Tarefa marcada como concluída.")

    def listar_tarefas(self):
        self.resultado.delete(1.0, tk.END)
        pendentes = self.usuario.listar_tarefas(concluidas=False)
        concluidas = self.usuario.listar_tarefas(concluidas=True)

        self.resultado.insert(tk.END, "📌 Tarefas Pendentes:\n")
        for t in pendentes:
            self.resultado.insert(tk.END, f" - {t}\n")

        self.resultado.insert(tk.END, "\n✅ Tarefas Concluídas:\n")
        for t in concluidas:
            self.resultado.insert(tk.END, f" - {t}\n")

    def mostrar_status(self):
        status = str(self.usuario)
        messagebox.showinfo("Status do Usuário", status)
