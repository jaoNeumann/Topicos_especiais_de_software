# ==========================
# Sistema de Gerenciamento de Livraria
# Entrega para matéria de Tópicos especiais do curso de sistemas de informação, 8º semestre
# ==========================

# Constante SELIC
DESCONTO_PADRAO = 0.105

# Lista de armazenagem de livros
livros = []

# Funções auxiliares para validação de entrada
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


# Metodo cadastrar
def cadastrar_livro():
    titulo = input_str("Título do livro: ")
    autor = input_str("Autor do livro: ")
    preco = input_float("Preço do livro (R$): ")
    estoque = input_int("Quantidade em estoque: ", minimo=0)

    livro = {"titulo": titulo, "autor": autor, "preco": preco, "estoque": estoque}
    livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso.\n")



# Metodo listar
def listar_livros():
    if not livros:
        print("⚠ Nenhum livro cadastrado ainda.\n")
        return
    print("\n📚 Livros disponíveis:")
    for i, livro in enumerate(livros):
        # 🔹 exibindo i+1 para não mostrar índice começando em 0
        print(
            f"{i+1} - {livro['titulo']} | Autor: {livro['autor']} | "
            f"Preço: R${livro['preco']:.2f} | Estoque: {livro['estoque']}"
        )
    print()


# Metodo vender
def realizar_venda():
    if not livros:
        print("⚠ Nenhum livro cadastrado para vender.\n")
        return

    listar_livros()

    indice = input_int("Digite o número do livro para vender: ", minimo=1, maximo=len(livros)) - 1
    livro = livros[indice]

    quantidade = input_int("Quantidade desejada: ", minimo=1)
    if quantidade > livro["estoque"]:
        print("⚠ Estoque insuficiente\n")
        return

    # Cálculo da venda
    valor_bruto = livro["preco"] * quantidade
    desconto = valor_bruto * DESCONTO_PADRAO if valor_bruto > 100 else 0
    valor_final = valor_bruto - desconto

    # Atualizar quantidade em estoque
    livro["estoque"] -= quantidade

    # Exibição de resumo da venda
    print("\n🧾 Resumo da Venda:")
    print(f"Livro: {livro['titulo']}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor bruto: R${valor_bruto:.2f}")
    if desconto > 0:
        print(f"Desconto aplicado ({DESCONTO_PADRAO * 100:.2f}%): R${desconto:.2f}")
    else:
        print("Sem desconto aplicado.")
    print(f"Valor final: R${valor_final:.2f}\n")
    print("Estoque atualizado\n")


# Menu principal
def menu():
    while True:
        print("====== Sistema de Livraria ======")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Realizar venda")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        print()

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            print("Encerrando o sistema. Volte sempre!")
            break
        else:
            print("⚠ Opção inválida. Digite apenas 1, 2, 3 ou 4.\n")


# Início do programa
menu()
