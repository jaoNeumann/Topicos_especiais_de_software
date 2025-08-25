DESCONTO_PADRAO = 0.105
roupas = []

def input_float(msg):
    while True:
        valor = input(msg)
        try:
            return float(valor)
        except ValueError:
            print("⚠ Entrada inválida. Digite um número decimal separado por ponto.")

def input_int(msg, minimo=None, maximo=None):
    while True:
        valor = input(msg)
        try:
            valor_int = int(valor)
            if (minimo is not None and valor_int < minimo) or (maximo is not None and valor_int > maximo):
                print(f"⚠ Digite um número entre {minimo} e {maximo}.")
                continue
            return valor_int
        except ValueError:
            print("⚠ Entrada inválida. Digite um número inteiro.")

def input_str(msg):
    while True:
        valor = input(msg).strip()
        if valor == "":
            print("⚠ Campo não pode ser vazio.")
        else:
            return valor

def cadastrar_roupa():
    nome = input_str("Nome da peça: ")
    tamanho = input_str("Tamanho (P, M, G, GG...): ")
    preco = input_float("Preço da peça (R$): ")
    estoque = input_int("Quantidade em estoque: ", minimo=0)

    roupa = {"nome": nome, "tamanho": tamanho, "preco": preco, "estoque": estoque}
    roupas.append(roupa)
    print(f"Peça '{nome}' cadastrada com sucesso.\n")

def listar_roupas():
    if not roupas:
        print("⚠ Nenhuma peça cadastrada ainda.\n")
        return
    print("\n👕 Peças disponíveis:")
    for i, roupa in enumerate(roupas):
        print(
            f"{i+1} - {roupa['nome']} | Tamanho: {roupa['tamanho']} | "
            f"Preço: R${roupa['preco']:.2f} | Estoque: {roupa['estoque']}"
        )
    print()

def realizar_venda():
    if not roupas:
        print("⚠ Nenhuma peça cadastrada para vender.\n")
        return

    listar_roupas()

    indice = input_int("Digite o número da peça para vender: ", minimo=1, maximo=len(roupas)) - 1
    roupa = roupas[indice]

    quantidade = input_int("Quantidade desejada: ", minimo=1)
    if quantidade > roupa["estoque"]:
        print("⚠ Estoque insuficiente\n")
        return

    valor_bruto = roupa["preco"] * quantidade
    desconto = valor_bruto * DESCONTO_PADRAO if valor_bruto > 100 else 0
    valor_final = valor_bruto - desconto

    roupa["estoque"] -= quantidade

    print("\n🧾 Resumo da Venda:")
    print(f"Peça: {roupa['nome']}")
    print(f"Tamanho: {roupa['tamanho']}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor bruto: R${valor_bruto:.2f}")
    if desconto > 0:
        print(f"Desconto aplicado ({DESCONTO_PADRAO * 100:.2f}%): R${desconto:.2f}")
    else:
        print("Sem desconto aplicado.")
    print(f"Valor final: R${valor_final:.2f}\n")
    print("Estoque atualizado\n")

def menu():
    while True:
        print("====== Sistema de Loja de Roupas ======")
        print("1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Realizar venda")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        print()

        if opcao == "1":
            cadastrar_roupa()
        elif opcao == "2":
            listar_roupas()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            print("Encerrando o sistema. Volte sempre!")
            break
        else:
            print("⚠ Opção inválida. Digite apenas 1, 2, 3 ou 4.\n")

menu()
