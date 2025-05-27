# 🧩 Gerenciador de Tarefas com Gamificação

Este projeto é um **gerenciador de tarefas com interface gráfica**, desenvolvido com foco em conceitos de **Orientação a Objetos**. Ele utiliza **elementos de gamificação** para motivar o usuário a concluir suas tarefas, acumulando pontos e subindo de nível a cada tarefa concluída.

## 🎯 Objetivo

Facilitar o gerenciamento de tarefas pessoais de forma divertida, intuitiva e produtiva, incentivando a organização e a constância através de recompensas simbólicas (pontos e níveis).

---

## 🧠 Funcionalidades

- ✅ **Cadastro de tarefas** com nome, descrição, prioridade e prazo
- 🔥 **Tarefas urgentes** que geram mais pontos
- 🧾 **Listagem de tarefas pendentes e concluídas**
- 🏅 **Sistema de pontuação e níveis**
- 💾 Dados mantidos em memória durante a sessão
- 🎨 Interface gráfica bonita com `tkinter`

---

## 👨‍💻 Tecnologias utilizadas

- Python 3
- `tkinter` (GUI nativa)
- Paradigma: **Programação Orientada a Objetos**
  - Herança
  - Polimorfismo
  - Composição
  - Associações fracas
  - Mixins (se desejado)
  - Encapsulamento

---

## 🗂️ Estrutura do projeto

```
gerenciador_tarefas/
├── main.py                 # Arquivo principal que inicia o app
├── interface_ui.py         # Interface gráfica com tkinter
└── package/
    ├── tarefa.py           # Classes Tarefa e TarefaUrgente
    ├── usuario.py          # Classe Usuario
    └── __init__.py
```

---

## 🚀 Como executar

1. Baixe/clique no repositório
2. Execute o seguinte comando no terminal:

```bash
python main.py
```

3. A interface será exibida com os campos para criar e concluir tarefas.

---

## 📚 Créditos

Projeto desenvolvido para a disciplina de **Orientação a Objetos - UnB Gama - 01/2025**  
Prof. Henrique Moura