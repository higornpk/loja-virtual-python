from modelos import Produto, Carrinho
import banco


def popular_produtos_iniciais():
    linhas = banco.listar_produtos()
    if linhas:
        return

    banco.inserir_produto("Camiseta", 49.90, 10)
    banco.inserir_produto("Calça Jeans", 129.90, 5)
    banco.inserir_produto("Tênis", 199.90, 3)
def carregar_produtos():
    linhas = banco.listar_produtos()

    lista_produtos = []
    for id_produto, nome, preco, estoque in linhas:
        produto = Produto(nome, preco, estoque)
        produto.id = id_produto
        lista_produtos.append(produto)

    return lista_produtos


banco.criar_tabelas()
popular_produtos_iniciais()
produtos = carregar_produtos()
carrinho = Carrinho()
carrinho.carregar_do_banco()


def linha(msg, caractere="="):
    tamanho = len(msg) + 10
    print(f"\n{caractere * tamanho}")
    print(f" {msg.center(tamanho)}")
    print(f"{caractere * tamanho}\n")
def cadastrar_produto():
    linha("Cadastrar novo produto", "-")
    nome = input("Nome: ")

    preco_texto = input("Preço: ")
    try:
        preco = float(preco_texto)
    except ValueError:
        print("\nPreço inválido. Use números, ex: 59.90")
        return
    # try/except em vez de isdigit(): preço tem casas decimais, e isdigit() só reconhece números inteiros.

    estoque_texto = input("Quantidade em estoque: ")
    if not estoque_texto.isdigit():
        print("\nEstoque inválido. Digite um número inteiro.")
        return
    estoque = int(estoque_texto)

    novo_produto = Produto(nome, preco, estoque)
    novo_produto.id = banco.inserir_produto(nome, preco, estoque)
    produtos.append(novo_produto)
    print(f"\n'{nome}' cadastrado com sucesso!")
def mostrar_produtos():
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. {produto}")
def adicionar_ao_carrinho():
    print()
    mostrar_produtos()

    escolha = input("\nDigite a opção do produto que deseja comprar: ")

    if not escolha.isdigit():
        print("\nEntrada inválida. Digite um número")
        return

    indice = int(escolha) - 1

    if indice < 0 or indice >= len(produtos):
        print("\nProduto não encontrado.")
        return

    produto = produtos[indice]

    if produto.estoque <= 0:
        print("\nProduto sem estoque")
        return

    carrinho.adicionar(produto)
    banco.atualizar_estoque(produto.id, produto.estoque)

    print(f"\n'{produto.nome}' adicionado ao carrinho!")
def ver_carrinho():
    if carrinho.esta_vazio():
        print("\nSeu carrinho está vazio.")
        return

    linha("Seu carrinho", "-")
    for produto in carrinho.itens:
        print(f"- {produto.nome} - R$ {produto.preco:.2f}")
    total = carrinho.calcular_total()

    print(f"\nTotal: R$ {total:.2f}")
def finalizar_compra():
    if carrinho.esta_vazio():
        print("\nSeu carrinho está vazio. Adicione produtos antes de finalizar a compra.")
        return

    ver_carrinho()
    confirmacao = input("\nDeseja confirmar a compra? (S/N): ").lower()

    if confirmacao == "s":
        linha("Compra finalizada com Sucesso!", "-")
        carrinho.limpar()
    else:
        print("Compra Cancelada.")


while True:
    linha("LOJA VIRTUAL")
    print("1. Ver produtos")
    print("2. Adicionar o produto ao carrinho")
    print("3. Ver carrinho")
    print("4. Finalizar compra")
    print("5. Cadastrar novo produto")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        linha("Lista de produtos", "-")
        mostrar_produtos()
    elif opcao == "2":
        adicionar_ao_carrinho()
    elif opcao == "3":
        ver_carrinho()
    elif opcao == "4":
        finalizar_compra()
    elif opcao == "5":
        cadastrar_produto()
    elif opcao == "6":
        print("\n Obrigado por visitar a loja!")
        break
    else:
        print("\n Opção inválida, tente novamente")