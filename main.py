
def menu():
    print("==============================")
    print("        CARD MANAGER")
    print("==============================")
    print()
    print("1 - Cadastrar carta manualmente")
    print("2 - Listar minha coleção")
    print("3 - Pesquisar carta na internet")
    print("4 - Pesquisar carta na minha coleção")
    print("5 - Remover carta da coleção")
    print("6 - Sair")
    print()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_carta()

    elif opcao == "2":
        print("Opção de listagem selecionada!")

    elif opcao == "3":
        print("Opção de pesquisa na internet selecionada!")

    elif opcao == "4":
        print("Opção de pesquisa na coleção selecionada!")

    elif opcao == "5":
        print("Opção de remoção selecionada!")

    elif opcao == "6":
        print("Encerrando o Card Manager...")

    else:
        print("Opção inválida! Tente novamente.")

    print()
    print("Você escolheu a opção:", opcao)


def cadastrar_carta():
    print("\n========== CADASTRAR CARTA ==========")

    nome = input("Nome da carta: ")

    print("\nEscolha o TCG:")
    print("1 - Pokemon TCG")
    print("2 - One Piece Card Game")
    print("3 - Magic: The Gathering")
    print("4 - Yu-Gi-Oh!")
    print("5 - Digimon Card Game")
    print("6 - Outros")

    opcao_jogo = input("Escolha uma opção: ")

    if opcao_jogo == "1":
        jogo = "Pokemon TCG"

    elif opcao_jogo == "2":
        jogo = "One Piece Card Game"

    elif opcao_jogo == "3":
        jogo = "Magic: The Gathering"

    elif opcao_jogo == "4":
        jogo = "Yu-Gi-Oh!"

    elif opcao_jogo == "5":
        jogo = "Digimon Card Game"

    elif opcao_jogo == "6":
        jogo = input("Digite o nome do TCG: ")

    else:
        print("Opção inválida!")
        return

    colecao = input("Coleção ou expansão: ")
    raridade = input("Raridade: ")
    quantidade = input("Quantidade: ")

    print("\nCarta cadastrada com sucesso!")
    print("Nome:", nome)
    print("Jogo:", jogo)
    print("Coleção:", colecao)
    print("Raridade:", raridade)
    print("Quantidade:", quantidade)


menu()
