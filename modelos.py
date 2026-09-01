import banco

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} (estoque: {self.estoque})"
class Carrinho:
    def __init__(self):
        self.itens = []
    def adicionar(self, produto):
        self.itens.append(produto)
        produto.estoque -= 1
        banco.inserir_item_carrinho(produto.id)
        # O carrinho referencia os mesmos objetos Produto já carregados, não cópias. Assim o estoque reflete a mesma instância em memória e no banco.
    def esta_vazio(self):
        return len(self.itens) == 0
    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco
        return total
    def limpar(self):
        self.itens.clear()
        banco.limpar_carrinho()
    def carregar_do_banco(self):
        linhas = banco.listar_itens_carrinho()
        for id_produto, nome, preco, estoque in linhas:
            produto = Produto(nome, preco, estoque)
            produto.id = id_produto
            self.itens.append(produto)

