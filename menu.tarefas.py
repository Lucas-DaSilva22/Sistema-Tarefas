tarefas = []

while True:
    print("\n===== MENU DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "4":
        print("Sistema encerrado.")
        break

    # Cadastrar tarefa
    elif opcao == "1":
        titulo = input("Digite o título da tarefa: ").strip()
        prioridade = input("Digite a prioridade (baixa, média ou alta): ").strip().lower()

        if titulo == "":
            print("O título não pode ser vazio.")

        elif prioridade not in ["baixa", "média", "alta"]:
            print("Prioridade inválida. Escolha baixa, média ou alta.")

        else:
            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }

            tarefas.append(tarefa)
            print("Tarefa cadastrada com sucesso.")

    # Listar tarefas
    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")

        else:
            print("\n===== TAREFAS =====")

            for i, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{i} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    # Para atualizar
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")

        else:
            numero = input(
                "Digite o número da tarefa que deseja concluir: "
            ).strip()

            if not numero.isdigit():
                print("Digite um número válido.")

            else:
                numero = int(numero)
                indice = numero - 1

                if indice < 0 or indice >= len(tarefas):
                    print("Tarefa inexistente.")

                else:
                    tarefas[indice]["situacao"] = "concluída"
                    print("Tarefa marcada como concluída.")
    else:
        print("Opção inválida. Escolha um número de 1 a 4.")