import random
from validacao import input_str, input_float, input_int, input_bool # 8.10 – Módulos

# 8.1 Variáveis locais e globais 
DESCONTO_PADRAO = 0.105
roupas = []

# 8.4 - Parâmetros Opcionais
def obter_tamanho_peca(tamanho_padrao='G'):
    tamanho = input(f"Tamanho (P, M, G, GG..., padrão é {tamanho_padrao}): ").strip()
    return tamanho if tamanho != '' else tamanho_padrao
# 8.7 – Empacotamento de parâmetros
def criar_roupa(**dados):
    return {
        "nome": dados.get("nome", "Sem nome"),
        "tamanho": dados.get("tamanho", "G"),
        "preco": dados.get("preco", 0.0),
        "estoque": dados.get("estoque", 0)
    }
# 8.12 - verificando os tipos
def cadastrar_roupa():
    nome = input_str("Nome da peça: ")
    tamanho = obter_tamanho_peca()
    preco = input_float("Preço da peça (R$): ")
    estoque = input_int("Quantidade em estoque: ", minimo=0)# 8.5 - Nomeando parâmetros

    # 8.12 - verificando os tipos
    print(f"\nTipos registrados: nome={type(nome)}, tamanho={type(tamanho)}, preco={type(preco)}, estoque={type(estoque)}\n")

    roupa = criar_roupa(**{
        "nome": nome,
        "tamanho": tamanho,
        "preco": preco,
        "estoque": estoque
    })

    roupas.append(roupa)
    print(f"Peça '{nome}' cadastrada com sucesso.\n")
# 8.6 - Funções como parâmetro
def listar_roupas(*roupas_para_listar, func_listar_roupa=None):
    if not roupas_para_listar:
        print("⚠ Nenhuma peça cadastrada ainda.\n")
        return
    for i, roupa in enumerate(roupas_para_listar):
        func_listar_roupa(i, roupa)
# 8.8 – Desempacotamento de parâmetros
def listar_roupa(i, roupa):
    print(
        f"{i+1} - {roupa['nome']} | Tamanho: {roupa['tamanho']} | "
        f"Preço: R${roupa['preco']:.2f} | Estoque: {roupa['estoque']}"
    )
# 8.9 - Funções Lambda
def listar_roupas_cadastradas():
    if not roupas:
        print("⚠ Nenhuma peça cadastrada ainda.\n")
        return

    roupas_ordenadas = sorted(roupas, key=lambda r: r["preco"])

    print("\n👕 Peças disponíveis (ordenadas por preço):")
    listar_roupas(
        *roupas_ordenadas,
        func_listar_roupa=lambda i, r: print(
            f"{i+1} - {r['nome']} | Tam: {r['tamanho']} | "
            f"Preço: R${r['preco']:.2f} | Estoque: {r['estoque']}"
        )
    )
    print()

def realizar_venda():
    if not roupas:
        print("⚠ Nenhuma peça cadastrada para vender.\n")
        return
    # 8.6 - Funções como parâmetro
    listar_roupas(*roupas, func_listar_roupa=listar_roupa)

    indice = input_int("Digite o número da peça para vender: ", minimo=1, maximo=len(roupas)) - 1
    roupa = roupas[indice]

    quantidade = input_int("Quantidade desejada: ", minimo=1)
    if quantidade > roupa["estoque"]:
        print("⚠ Estoque insuficiente\n")
        return
    
    tem_desconto_personalizado = input_bool('Deseja desconto personalizado? [S/N] ')
    # 8.1 - Variáveis locais e globais
    if tem_desconto_personalizado:
        desconto = input_float('Qual o valor do desconto (ex: 0.10 para 10%)? ')
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
        print(f"Desconto aplicado: R${desconto_aplicado:.2f}")
    else:
        print("Sem desconto aplicado.")
    print(f"Valor final: R${valor_final:.2f}\n")
    print("Estoque atualizado\n")
# 8.11 - escolher aleatoriamente uma roupa cadastrada
def compra_aleatoria():
    if not roupas:
        print("⚠ Nenhuma peça cadastrada ainda para compra aleatória.\n")
        return

    # 8.11 - escolher aleatoriamente uma roupa cadastrada
    roupa = random.choice(roupas)

    if roupa["estoque"] <= 0:
        print(f"⚠ O item '{roupa['nome']}' não tem estoque disponível.\n")
        return

    # compra sempre 1 unidade
    quantidade = 1
    valor_bruto = roupa["preco"] * quantidade
    valor_final = valor_bruto  # sem desconto, é só exemplo de usabilidade do item 8.11

    roupa["estoque"] -= quantidade

    print("\n🎲 Compra Aleatória Realizada!")
    print(f"Peça: {roupa['nome']}")
    print(f"Tamanho: {roupa['tamanho']}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor pago: R${valor_final:.2f}")
    print("Estoque atualizado.\n")