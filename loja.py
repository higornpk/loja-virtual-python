import os
import sqlite3

class Produto:
#Criando defs que serão acionadas quando chamarem a classe Produto.

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} (estoque: {self.estoque})"
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar (self, produto):
        self.itens.append(produto)
        produto.estoque -= 1
        inserir_item_carrinho_banco(produto)

    def esta_vazio(self):
        return len(self.itens) == 0

    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco
        return total

    def limpar(self):
        self.itens.clear()
        limpar_carrinho_banco()

    def carregar_do_banco(self):
        linhas = listar_itens_carrinho_banco()
        for id_produto, nome, preco, estoque in linhas:
            produto = Produto(nome, preco,estoque)
            produto.id = id_produto
            self.itens.append(produto)
    
NOME_BANCO = "loja.db"


def criar_tabelas():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )    
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carrinho (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
        )
    """)

    conexao.commit()
    conexao.close()
def inserir_produto_banco(produto):
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, preco, estoque) Values (?, ?, ?)",
        (produto.nome, produto.preco, produto.estoque)
    )

    conexao.commit()
    conexao.close()
def listar_produtos_banco():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, preco, estoque FROM produtos")
    linhas = cursor.fetchall()

    conexao.close()
    return linhas
def popular_produtos_iniciais():
    linhas = listar_produtos_banco()
    if linhas:
        return

    inserir_produto_banco(Produto("Camiseta", 49.90, 10))
    inserir_produto_banco(Produto("calça jeans", 129.90, 5))
    inserir_produto_banco(Produto("Tênis", 199.90, 3))
def carregar_produtos_banco():
    linhas = listar_produtos_banco()

    lista_produtos = []
    for linha_produto in linhas:
        id_produto, nome, preco, estoque = linha_produto
        produto = Produto(nome, preco, estoque)
        produto.id = id_produto
        lista_produtos.append(produto)  

    return lista_produtos
def atualizar_estoque_banco(produto):
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE produtos set estoque = ? WHERE id = ?", (produto.estoque, produto.id)
    )

    conexao.commit()
    conexao.close()
def cadastrar_produto_banco(produto):
    inserir_produto_banco(produto)

    linhas = listar_produtos_banco()
    ultima_linha = linhas[-1]
    produto.id = ultima_linha[0]
def inserir_item_carrinho_banco(produto):
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO carrinho (produto_id) VALUES (?)", (produto.id,)
    )

    conexao.commit()
    conexao.close()
def listar_itens_carrinho_banco():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT produtos.id, produtos.nome, produtos.preco, produtos.estoque
        FROM carrinho
        JOIN produtos on carrinho.produto_id = produtos.id
    """)
    linhas = cursor.fetchall()

    conexao.close()
    return linhas
def limpar_carrinho_banco():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM carrinho")

    conexao.commit
    conexao.close()


criar_tabelas()
popular_produtos_iniciais()
produtos = carregar_produtos_banco()

carrinho = Carrinho()
carrinho.carregar_do_banco()



def linha(msg, caractere = "="):
    tamanho = len(msg) + 10
    print(f"\n{caractere * tamanho}")
    print(f" {msg.center(tamanho)}")
    print(f"{caractere * tamanho}\n")

    #Função para nao precisar reescrever toda vez que for fazer um titulo  
def cadastrar_produto():
    linha ("Cadastrar novo produto", "-")
    nome = input("Nome: ")

    preco_texto = input("Preço: ")
    try:
        preco = float(preco_texto)
    except ValueError:
        print("\nPreço inválido. Use números, ex: 59.90")
        return

    estoque_texto = input("Quantidade em estoque: ")
    if not estoque_texto.isdigit():
        print("\nEstoque inválido. Digite um número inteiro.")
        return
    estoque = int(estoque_texto)

    novo_produto = Produto(nome, preco, estoque)
    produtos.append(novo_produto)
    cadastrar_produto_banco(novo_produto)
    print(f"\n'{nome}' cadastrado com sucesso!")
def mostrar_produtos():
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. {produto}")
    # for i, produto in enumerate(produtos): è um loop que repete um bloco de códigos para cada item da lista produtos, usando a função enumerate() que entrega a cada volta desse looping dois valores que sâo: o indice(posição) e o item, por isso as variáveis i -> que recebe o indice e o produto -> que recebe o item relacionado ao indice
def adicionar_ao_carrinho():
    print()
    mostrar_produtos()

    escolha = input("\nDigite a opção do produto que deseja comprar: ")

    if not escolha.isdigit():
        print("\nEntrada inválida. Digite um número")
        return
        #Verifica se o texto e composto só por números

    indice = int(escolha) - 1
        # coverte o texto digitado em número inteiro, para poder usar como indice da lista

    if indice < 0 or indice >= len(produtos):
        print("\nProduto não encontrado.")
        return
        #conta quantos itens tem na lista, verificando se o número escolhido está fora dos limites da lista
    
    produto = produtos[indice]

    if produto.estoque <= 0:
        print("\nProduto sem estoque")
        return

    carrinho.adicionar(produto)
    atualizar_estoque_banco(produto)

    print(f"\n'{produto.nome}' adicionado ao carrinho!")
def ver_carrinho():
    if carrinho.esta_vazio():
        print("\nSeu carrinho está vazio.")
        return
        #verifica se o carrinho esta vazio e retorna o print caso esteja.

    linha("Seu carrinho", "-")
    total = 0 # variavel acumuladora, para ir somando os preços conforme o loop passa por cada produto
    for produto in carrinho.itens:
        print(f"- {produto.nome} - R$ {produto.preco:.2f}")
    total = carrinho.calcular_total()

    print(f"\nTotal: R$ {total:.2f}")
def finalizar_compra():
    if carrinho.esta_vazio():
        print(f"\nSeu carrinho está vazio. Adicione produtos antes de finalizar a compra.")
        return

    ver_carrinho()
    confirmacao = input("\nDeseja confirmar a compra? (S/N): ").lower()

    if confirmacao == "s":
        linha("Compra finalizada com Sucesso!", "-")
        carrinho.limpar()
    else:
        print("Compra Cancelada.")
        
while True:

    linha("LOJA VITUAL")
    print("1. Ver produtos")
    print("2. Adicionar o produto ao carrinho")
    print("3. Ver carrinho")
    print("4. Finalizar compra")
    print("5. Cadastrar novo produto")
    print("6. Sair")

    #Menu principal da loja

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        linha("Lista de produtos", '-')
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


    

