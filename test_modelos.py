from modelos import Produto, Carrinho


def test_calcular_total_carrinho_vazio():
    carrinho = Carrinho()
    assert carrinho.calcular_total() == 0


def test_calcular_total_com_itens():
    carrinho = Carrinho()
    carrinho.itens.append(Produto("Caneta", 2.50, 10))
    carrinho.itens.append(Produto("Caderno", 15.00, 5))

    assert carrinho.calcular_total() == 17.50


def test_carrinho_esta_vazio_quando_criado():
    carrinho = Carrinho()
    assert carrinho.esta_vazio() is True


def test_carrinho_nao_esta_vazio_apos_adicionar_item():
    carrinho = Carrinho()
    carrinho.itens.append(Produto("Caneta", 2.50, 10))
    assert carrinho.esta_vazio() is False


def test_produto_str_formata_corretamente():
    produto = Produto("Caneta", 2.50, 10)
    assert str(produto) == "Caneta - R$ 2.50 (estoque: 10)"