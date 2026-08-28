import json
import os


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

    def esta_vazio(self):
        return len(self.itens) == 0

    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco
        return total

    def limpar(self):
        self.itens.clear()

    def salvar(self):
        nomes = [produto.nome for produto in self.itens]
        with open(ARQUIVO_CARRINHO, "w", encoding="utf-8") as arquivo:
            json.dump(nomes, arquivo, indent=4, ensure_ascii=False)

    def carregar(self, lista_produtos):
        if not os.path.exists(ARQUIVO_CARRINHO):
            return

        with open(ARQUIVO_CARRINHO, "r", encoding="utf-8") as arquivo:
            nomes = json.load(arquivo)

        for nome in nomes:
            for produto in lista_produtos:
                if produto.nome == nome:
                    self.itens.append(produto)
                    break

    

ARQUIVO_PRODUTOS = "produtos.json"
ARQUIVO_CARRINHO = "    carrinho.json"

def carregar_produtos():
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return [
            Produto("Camiseta", 49.90, 10),
            Produto("Calça jeans", 129.90, 5),
            Produto("Tênis", 199.90, 3),
         ]

    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    lista_produtos = []
    for item in dados:
        lista_produtos.append(Produto(item["nome"], item["preco"], item["estoque"]))

    return lista_produtos 
def salvar_produtos():
    dados = []
    for produto in produtos:
        dados.append({"nome": produto.nome, "preco": produto.preco, "estoque": produto.estoque})

    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


produtos = carregar_produtos()
carrinho = Carrinho()
carrinho.carregar(produtos)

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
        carrinho.salvar()
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
        salvar_produtos()
        carrinho.salvar()
    elif opcao == "3":
        ver_carrinho()
    elif opcao == "4":
        finalizar_compra()
    elif opcao == "5":
        cadastrar_produto()
        salvar_produtos()
    elif opcao == "6":
        print("\n Obrigado por visitar a loja!")
        break

    else:
        print("\n Opção inválida, tente novamente")

