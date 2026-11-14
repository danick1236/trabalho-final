def menu_inicial():
    print("==============================")
    print("        CARD MANAGER")
    print("==============================")
    print()
    print("1 - Fazer login")
    print("2 - Cadastrar usuario")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        usuario_logado = login()

        if usuario_logado != None:
            menu(usuario_logado)

    elif opcao == "2":
        cadastrar_usuario()

    elif opcao == "3":
        print("Encerrando o Card Manager...")

    else:
        print("Opção inválida!")

def menu(usuario_logado):
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
        cadastrar_carta(usuario_logado)

    elif opcao == "2":
        listar_cartas(usuario_logado)

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


def cadastrar_carta(usuario_logado):
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

    arquivo = open("colecoes/" + usuario_logado + ".txt", "a")

    arquivo.write(nome + ";" + jogo + ";" + colecao + ";" + raridade + ";" + quantidade + "\n")

    arquivo.close()

    print("\nCarta cadastrada com sucesso!")
    print("Nome:", nome)
    print("Jogo:", jogo)
    print("Coleção:", colecao)
    print("Raridade:", raridade)
    print("Quantidade:", quantidade)


def listar_cartas(usuario_logado):
    print("\n========== MINHA COLECAO ==========")

    arquivo = open("colecoes/" + usuario_logado + ".txt", "r")

    encontrou = False

    for linha in arquivo:
        dados = linha.strip().split(";")

        print("\nNome:", dados[0])
        print("Jogo:", dados[1])
        print("Coleção:", dados[2])
        print("Raridade:", dados[3])
        print("Quantidade:", dados[4])

        encontrou = True

    arquivo.close()

    if encontrou == False:
        print("\nSua coleção está vazia!")




def cadastrar_usuario():
    print("\n===== CADASTRO DE USUARIO =====")

    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    arquivo = open("usuarios.txt", "a")
    arquivo.write(usuario + ";" + senha + "\n")
    arquivo.close()

    print("\nUsuario cadastrado com sucesso!")

    def login():
    print("\n===== LOGIN =====")

    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    arquivo = open("usuarios.txt", "r")

    for linha in arquivo:
        dados = linha.strip().split(";")

        if dados[0] == usuario and dados[1] == senha:
            arquivo.close()
            print("\nLogin realizado com sucesso!")
            return usuario

    arquivo.close()

    print("\nUsuario ou senha incorretos!")
    return None

menu_inicial()