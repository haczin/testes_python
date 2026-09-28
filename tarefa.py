tarefas = ["email chefe", "corriga o bug", "atendendo chamado"]

for tarefas in tarefas:
    if tarefas == "corriga o bug":
        print("Tarefa urgente: corriga o bug ")
        break
    print(f"Trabalhando em: {tarefas}")
