from datetime import datetime, timedelta

# Lista de vendas
vendas = []

# Exemplo de produtos (pode integrar com seu sistema)
produtos = [
    {"codigo": 1, "nome": "pão", "valor_venda": 15.0},
    {"codigo": 2, "nome": "cuca tradicional", "valor_venda": 35.0},
    {"codigo": 3, "nome": "geleia de morango", "valor_venda": 45.0}
]


def buscar_produto(nome):
    nome = nome.lower()
    for p in produtos:
        if p["nome"] == nome:
            return p
    return None


# REGISTRAR VENDA
def registrar_venda():
    nome = input("Produto vendido: ").strip().lower()
    produto = buscar_produto(nome)

    if not produto:
        print("Produto não encontrado.")
        return

    qtd = input("Quantidade vendida: ")

    if not qtd.isdigit():
        print("Quantidade inválida.")
        return

    qtd = int(qtd)

    if qtd <= 0:
        print("Quantidade deve ser maior que zero.")
        return

    venda = {
        "produto": produto["nome"],
        "quantidade": qtd,
        "valor_unitario": produto["valor_venda"],
        "data": datetime.now()
    }

    vendas.append(venda)

    print("Venda registrada com sucesso!")


# FILTRAR VENDAS POR PERÍODO
def filtrar_vendas(dias):
    limite = datetime.now() - timedelta(days=dias)

    return [v for v in vendas if v["data"] >= limite]


# GERAR RELATÓRIO
def gerar_relatorio(tipo):
    if tipo == "diario":
        dados = filtrar_vendas(1)
    elif tipo == "semanal":
        dados = filtrar_vendas(7)
    elif tipo == "mensal":
        dados = filtrar_vendas(30)
    else:
        print("Tipo inválido")
        return

    total = 0

    print(f"\n--- RELATÓRIO {tipo.upper()} ---")

    if not dados:
        print("Nenhuma venda encontrada.")
        return

    for v in dados:
        valor_total = v["quantidade"] * v["valor_unitario"]
        total += valor_total

        print(
            f"{v['produto']} | "
            f"Qtd: {v['quantidade']} | "
            f"R$ {valor_total:.2f} | "
            f"{v['data'].strftime('%d/%m/%Y %H:%M')}"
        )

    print(f"\nTOTAL VENDIDO: R$ {total:.2f}")


# MENU
while True:
    print("\n===== VENDAS =====")
    print("1 - Registrar venda")
    print("2 - Relatório diário")
    print("3 - Relatório semanal")
    print("4 - Relatório mensal")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        registrar_venda()
    elif op == "2":
        gerar_relatorio("diario")
    elif op == "3":
        gerar_relatorio("semanal")
    elif op == "4":
        gerar_relatorio("mensal")
    elif op == "0":
        break
    else:
        print("Opção inválida.")