# SISTEMA DE CONTROLE DE ESTOQUE

produtos = [
    {
        "codigo": 1,
        "nome": "pão",
        "descricao": "Pão caseiro tradicional",
        "custo": 20.00,
        "valor_venda": 15.00,
        "estoque": 50,
        "imagem": "imagens/pao.jpg"
    },
    {
        "codigo": 2,
        "nome": "cuca tradicional",
        "descricao": "Cuca tradicional com farofa",
        "custo": 25.50,
        "valor_venda": 35.00,
        "estoque": 50,
        "imagem": "imagens/cuca.jpg"
    },
    {
        "codigo": 3,
        "nome": "geleia de morango",
        "descricao": "Geleia artesanal de morango",
        "custo": 18.00,
        "valor_venda": 45.00,
        "estoque": 50,
        "imagem": "imagens/geleia.jpg"
    }
]


def listar_produtos():
    print("\n----- LISTA DE PRODUTOS -----")

    for produto in produtos:
        print(f"\nCódigo: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Custo: R$ {produto['custo']:.2f}")
        print(f"Valor de venda: R$ {produto['valor_venda']:.2f}")
        print(f"Estoque disponível: {produto['estoque']}")
        print(f"Imagem: {produto['imagem']}")


def buscar_produto(nome):
    nome = nome.strip().lower()

    for produto in produtos:
        if produto["nome"].lower() == nome:
            return produto

    return None


def consultar_estoque():
    nome = input("Digite o nome do produto: ")

    produto = buscar_produto(nome)

    if produto:
        print("\nProduto encontrado:")
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Custo: R$ {produto['custo']:.2f}")
        print(f"Valor de venda: R$ {produto['valor_venda']:.2f}")
        print(f"Estoque disponível: {produto['estoque']}")
        print(f"Imagem: {produto['imagem']}")

    else:
        print("Produto não encontrado.")


def entrada_produto():
    nome = input("Digite o nome do produto: ")

    produto = buscar_produto(nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade = input("Digite a quantidade recebida: ")

    if not quantidade.isdigit():
        print("Quantidade inválida.")
        return

    quantidade = int(quantidade)

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    produto["estoque"] += quantidade

    print("Entrada registrada com sucesso.")
    print(f"Novo estoque: {produto['estoque']}")


def saida_produto():
    nome = input("Digite o nome do produto: ")

    produto = buscar_produto(nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade = input("Digite a quantidade retirada: ")

    if not quantidade.isdigit():
        print("Quantidade inválida.")
        return

    quantidade = int(quantidade)

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    if quantidade <= produto["estoque"]:
        produto["estoque"] -= quantidade

        print("Saída registrada com sucesso.")
        print(f"Novo estoque: {produto['estoque']}")

    else:
        print("Estoque insuficiente.")


def estoque_baixo():
    print("\n----- PRODUTOS COM ESTOQUE BAIXO -----")

    encontrou = False

    for produto in produtos:
        if produto["estoque"] < 15:
            print(
                f"{produto['nome']} - "
                f"Estoque: {produto['estoque']}"
            )

            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")


while True:

    print("\n==============================")
    print("     CONTROLE DE ESTOQUE")
    print("==============================")

    print("1 - Listar produtos")
    print("2 - Consultar produto")
    print("3 - Entrada de produtos")
    print("4 - Saída de produtos")
    print("5 - Produtos com estoque baixo")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("Encerrando o sistema...")
        break

    elif opcao == "1":
        listar_produtos()

    elif opcao == "2":
        consultar_estoque()

    elif opcao == "3":
        entrada_produto()

    elif opcao == "4":
        saida_produto()

    elif opcao == "5":
        estoque_baixo()

    else:
        print("Opção inválida.")