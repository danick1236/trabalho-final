import requests

def menu_inicial():
    opcao = ""

    while opcao != "3":
        print("\n==============================")
        print("        CARD MANAGER")
        print("==============================")
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
    opcao = ""

    while opcao != "6":
        print("\n==============================")
        print("        CARD MANAGER")
        print("==============================")
        print("1 - Cadastrar carta manualmente")
        print("2 - Listar minha coleção")
        print("3 - Pesquisar carta na internet")
        print("4 - Pesquisar carta na minha coleção")
        print("5 - Remover carta da coleção")
        print("6 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_carta(usuario_logado)

        elif opcao == "2":
            listar_cartas(usuario_logado)

        elif opcao == "3":
            pesquisar_internet()

        elif opcao == "4":
            pesquisar_carta(usuario_logado)

        elif opcao == "5":
            remover_carta(usuario_logado)

        elif opcao == "6":
            print("Saindo da coleção...")

        else:
            print("Opção inválida!")

        if opcao != "6":
            input("\nPressione ENTER para voltar ao menu...")


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

def pesquisar_carta(usuario_logado):
    print("\n========== PESQUISAR CARTA ==========")

    pesquisa = input("Digite o nome da carta: ").strip().lower()

    if pesquisa == "":
        print("Digite um nome para pesquisar!")
        return

    arquivo = open("colecoes/" + usuario_logado + ".txt", "r")

    encontrou = False

    for linha in arquivo:
        dados = linha.strip().split(";")

        nome = dados[0]

        if pesquisa in nome.lower():
            print("\nNome:", dados[0])
            print("Jogo:", dados[1])
            print("Coleção:", dados[2])
            print("Raridade:", dados[3])
            print("Quantidade:", dados[4])

            encontrou = True

    arquivo.close()

    if encontrou == False:
        print("\nNenhuma carta encontrada!")


def pesquisar_internet():
    print("\n========== PESQUISAR NA INTERNET ==========")

    print("1 - Pokemon TCG")
    print("2 - One Piece Card Game")
    print("3 - Magic: The Gathering")
    print("4 - Yu-Gi-Oh!")
    print("5 - Digimon Card Game")

    opcao = input("Escolha o TCG: ")

    if opcao == "1":
        jogo = "pokemon"
    elif opcao == "2":
        jogo = "one-piece"
    elif opcao == "3":
        jogo = "magic"
    elif opcao == "4":
        jogo = "yugioh"
    elif opcao == "5":
        jogo = "digimon"
    else:
        print("Opção inválida!")
        return

    nome = input("Digite o nome da carta: ").strip()

    if nome == "":
        print("Digite o nome de uma carta!")
        return

    arquivo = open("chave_api.txt", "r")
    chave = arquivo.read().strip()
    arquivo.close()

    url = "https://api.apitcg.com/api/products"

    parametros = {
        "tcg": jogo,
        "type": "card",
        "name": nome,
        "limit": 5
    }

    cabecalho = {"x-api-key": chave}

    try:
        resposta = requests.get(
            url,
            params=parametros,
            headers=cabecalho,
            timeout=15
        )

        if resposta.status_code == 401:
            print("\nA API não autorizou sua chave.")
            print("Detalhes:", resposta.text[:300])
            return
        
        resposta.raise_for_status()
        resultado = resposta.json()

        cartas = resultado.get("data", [])

        if not cartas:
            print("\nNenhuma carta encontrada!")
            return

        print("\n========== RESULTADOS ==========")

        for carta in cartas:
            nome = carta.get("name", "Não informado")

            tcg = carta.get("tcg") or {}
            jogo = tcg.get("name", "Não informado")

            conjunto = carta.get("set") or {}
            colecao = conjunto.get("name", "Não informado")

            codigo = carta.get("code") or "Não informado"

            atributos = carta.get("attributes") or {}
            raridade = atributos.get("Rarity", "Não informado")

            print("\n------------------------------")
            print("Nome:", nome)
            print("Jogo:", jogo)
            print("Coleção:", colecao)
            print("Código:", codigo)
            print("Raridade:", raridade)

    except requests.exceptions.RequestException as erro:
        print("\nErro ao consultar a internet:", erro)

    except ValueError:
        print("\nNão foi possível interpretar a resposta.")


def remover_carta(usuario_logado):
    print("\n========== REMOVER CARTA ==========")

    nome = input("Digite o nome da carta: ").strip()

    if nome == "":
        print("Digite o nome de uma carta!")
        return

    caminho = "colecoes/" + usuario_logado + ".txt"

    arquivo = open(caminho, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    cartas_restantes = []
    encontrou = False

    for linha in linhas:
        dados = linha.strip().split(";")

        if dados[0].lower() == nome.lower():
            print("\nCarta encontrada:")
            print("Nome:", dados[0])
            print("Jogo:", dados[1])
            print("Coleção:", dados[2])
            print("Raridade:", dados[3])
            print("Quantidade:", dados[4])

            encontrou = True

        else:
            cartas_restantes.append(linha)

    if encontrou == False:
        print("\nCarta não encontrada!")
        return

    confirmar = input("\nDeseja realmente remover? (s/n): ")

    if confirmar.lower() == "s":
        arquivo = open(caminho, "w")
        arquivo.writelines(cartas_restantes)
        arquivo.close()

        print("\nCarta removida com sucesso!")

    else:
        print("\nRemoção cancelada!")



def cadastrar_usuario():
    print("\n===== CADASTRO DE USUARIO =====")

    usuario = input("Digite seu usuario: ").strip()
    senha = input("Digite sua senha: ")

    if usuario == "" or senha == "":
        print("Usuario e senha não podem estar vazios!")
        return

    if not usuario.isalnum():
        print("O usuario deve conter apenas letras e numeros!")
        return

    arquivo = open("usuarios.txt", "a+")
    arquivo.seek(0)

    for linha in arquivo:
        dados = linha.strip().split(";")

        if dados[0].lower() == usuario.lower():
            print("Esse usuario ja existe!")
            arquivo.close()
            return

    arquivo.write(usuario + ";" + senha + "\n")
    arquivo.close()

    arquivo = open("colecoes/" + usuario + ".txt", "a")
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