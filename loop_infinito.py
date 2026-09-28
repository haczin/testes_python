tarefas = ["pendente", "completa", "pendente", "pendente"]
index = 0 

while index < len(tarefas):
    if tarefas[index] == "completa":
        print(f"pulando tarefa {index + 1}")
        index += 1
        continue
        print(f"processando tarefa {index + 1}")
        index += 1
