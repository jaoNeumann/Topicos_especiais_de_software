DESCONTO_PADRAO = 0.105
desconto = DESCONTO_PADRAO
roupas = []

# 8.3 - Validação
def input_float(msg):
    while True:
        valor = input(msg)
        try:
            return float(valor)
        except ValueError:
            print("⚠ Entrada inválida. Digite um número decimal separado por ponto.")

# 8.3 - Validação
# 8.5 - Nomeando parâmetros
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

# 8.3 - Validação
def input_str(msg):
    while True:
        valor = input(msg).strip()
        if valor == "":
            print("⚠ Campo não pode ser vazio.")
        else:
            return valor
        
# 8.3 - Validação
def input_bool(msg):
    while True:
        valor = input(msg).strip().upper()
        
        if valor == 'S':
            return True
        
        if valor == 'N':
            return False

        print("⚠ Campo só pode conter 'S' ou 'N'.")

# 8.4 - Parâmetros Opcionais
def obter_tamanho_peca(tamanho_padrao = 'G'):
    tamanho = input(f"Tamanho (P, M, G, GG..., padrão é {tamanho_padrao}): ").strip()
    return tamanho == '' if tamanho else tamanho_padrao 

def cadastrar_roupa():
    nome = input_str("Nome da peça: ")
    tamanho = obter_tamanho_peca() # 8.4 - Parâmetros Opcionais
    preco = input_float("Preço da peça (R$): ")
    estoque = input_int("Quantidade em estoque: ", minimo=0) # 8.5 - Nomeando parâmetros

    roupa = {"nome": nome, "tamanho": tamanho, "preco": preco, "estoque": estoque}
    roupas.append(roupa)
    print(f"Peça '{nome}' cadastrada com sucesso.\n")

# 8.6 - Funções como parâmetro
def listar_roupas(*roupas_para_listar, func_listar_roupa=None):
    if not roupas_para_listar:
        print("⚠ Nenhuma peça cadastrada ainda.\n")
        return
    print("\n👕 Peças disponíveis:")
    for i, roupa in enumerate(roupas_para_listar):
        func_listar_roupa(i, roupa)

    print()

def listar_roupa(i, roupa):
    print(
        f"{i+1} - {roupa['nome']} | Tamanho: {roupa['tamanho']} | "
        f"Preço: R${roupa['preco']:.2f} | Estoque: {roupa['estoque']}"
    )

def realizar_venda():
    if not roupas:
        print("⚠ Nenhuma peça cadastrada para vender.\n")
        return

    # 8.6 - Funções como parâmetro
    listar_roupas(*roupas, func_listar_roupa=listar_roupa)

    # 8.5 - Nomeando parâmetros
    indice = input_int("Digite o número da peça para vender: ", minimo=1, maximo=len(roupas)) - 1
    roupa = roupas[indice]

    quantidade = input_int("Quantidade desejada: ", minimo=1)
    if quantidade > roupa["estoque"]:
        print("⚠ Estoque insuficiente\n")
        return
    

    tem_desconto_personalizado = input_bool('Deseja desconto personalizado? [S/N]')
    
    # 8.1 - Variáveis locais e globais
    if tem_desconto_personalizado:
        desconto = input_float('Qual o valor do desconto? ')
    else:
        desconto = DESCONTO_PADRAO

    valor_bruto = roupa["preco"] * quantidade
    desconto_aplicado = valor_bruto * desconto if valor_bruto > 100 else 0
    valor_final = valor_bruto - desconto_aplicado

    roupa["estoque"] -= quantidade

    print("\n🧾 Resumo da Venda:")
    print(f"Peça: {roupa['nome']}")
    print(f"Tamanho: {roupa['tamanho']}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor bruto: R${valor_bruto:.2f}")
    if desconto > 0:
        print(f"Desconto aplicado ({desconto * 100:.2f}%): R${desconto_aplicado:.2f}")
    else:
        print("Sem desconto aplicado.")
    print(f"Valor final: R${valor_final:.2f}\n")
    print("Estoque atualizado\n")

def menu():
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
        return
    else:
        print("⚠ Opção inválida. Digite apenas 1, 2, 3 ou 4.\n")

    menu() # 8.2 - Funções RECURSIVAS

menu()