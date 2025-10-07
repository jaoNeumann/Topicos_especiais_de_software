# 📚 Sistema de Gerenciamento de Livraria

Um mini-sistema em **Python** desenvolvido para simular o gerenciamento
de uma livraria.\
Permite **cadastrar, listar e vender livros**, com controle de estoque e
aplicação automática de desconto em compras acima de R\$100,00.

## 🚀 Como usar

1.  Execute o arquivo principal:

    ``` bash
    python livraria.py
    ```

2.  Escolha uma das opções do menu:

    -   **1** → Cadastrar um novo livro\
    -   **2** → Listar todos os livros cadastrados\
    -   **3** → Realizar uma venda\
    -   **4** → Encerrar o programa

3.  Durante a venda:

    -   Escolha o livro pelo número da lista\
    -   Informe a quantidade desejada\
    -   O sistema calcula automaticamente o valor total, aplica desconto
        (se aplicável) e atualiza o estoque.

## ⚙️ Regras e validações

-   Não é possível vender mais do que o estoque disponível.\
-   O desconto é aplicado apenas em compras acima de **R\$100,00**.\
-   Tipos de dados são verificados com `isinstance()` para evitar
    erros.\
-   Após cada venda, o estoque é atualizado automaticamente.

## 🧩 Estrutura

O sistema foi construído de forma simples e modular, com funções
separadas para cada ação: - `cadastrar_livro()`\
- `listar_livros()`\
- `realizar_venda()`\
- `menu()` (controla o fluxo principal)
