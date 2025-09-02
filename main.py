from loja import cadastrar_roupa, listar_roupas_cadastradas, realizar_venda, compra_aleatoria # 8.10 – Módulos

def menu():
    print("====== Sistema de Loja de Roupas ======")
    print("1 - Cadastrar peça")
    print("2 - Listar peças")
    print("3 - Realizar venda")
    print("4 - Sair")
    print("6 - Compra aleatória")


    opcao = input("Escolha uma opção: ").strip()
    print()

    if opcao == "1":
        cadastrar_roupa()
    elif opcao == "2":
        listar_roupas_cadastradas()
    elif opcao == "3":
        realizar_venda()
    elif opcao == "4":
        print("Encerrando o sistema. Volte sempre!")
        return
    elif opcao == "6":
        compra_aleatoria()
    else:
        print("⚠ Opção inválida. Digite apenas 1, 2, 3, 4 ou 6.\n")

    menu()  # recursividade (8.2)


if __name__ == "__main__":
    menu()
