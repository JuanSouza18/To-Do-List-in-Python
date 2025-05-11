tarefas = []

def exibir_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def menu():
    while True:
        print("\n Menu ")
        print("1. Adicionar Nova Tarefa")
        print("2. Alterar Tarefa")
        print("3. Remover Tarefa")
        print("4. Exibir Tarefas")
        print("5. Sair")

        option = input("Digite a opção desejada: ")

        if option == "1":
            tarefa = input('Qual tarefa você deseja adicionar? ')
            tarefas.append(tarefa)
            print(f'Tarefa adicionada: {tarefa}')

        elif option == "2":
            exibir_tarefas()
            indice = input("Número da tarefa para alterar: ")

            if indice.isdigit() and 1 <= int(indice) <= len(tarefas):
                indice = int(indice) - 1
                nova_tarefa = input("Digite a nova tarefa: ")
                tarefas[indice] = nova_tarefa
                print("Tarefa alterada com sucesso.")
            else:
                print("Opção inválida!")

        elif option == "3":
            exibir_tarefas()
            indice = input("Número da tarefa para remover: ")

            if indice.isdigit() and 1 <= int(indice) <= len(tarefas):
                indice = int(indice) - 1
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa removida: {tarefa_removida}")
            else:
                print("Opção inválida!")

        elif option == "4":
            exibir_tarefas()

        elif option == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

menu()
