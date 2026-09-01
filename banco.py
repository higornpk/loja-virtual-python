import sqlite3

NOME_BANCO = "loja.db"

def criar_tabelas():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute ("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    """)

    cursor.execute ("""
        CREATE TABLE IF NOT EXISTS carrinho (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
        )
    """)

    # Guardamos só o produto_id (chave estrangeira), não os dados do produto duplicados aqui. Os detalhes (nome, preço) sempre vêm de produtos via JOIN.

    conexao.commit()
    conexao.close()
def inserir_produto(nome, preco, estoque):
    conexao = sqlite3.connetc(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", 
        (nome, preco, estoque)
    )

    conexao.commit()
    conexao.close()
    return cursor.lastrowid
    # Query parametrizada (com ?) em vez de concatenar string. Evita SQL Injection e trata os valores com segurança.
    # lastrowid retorna o id gerado pelo AUTOINCREMENT na inserção mais recente desta conexão. Mais direto e seguro do que buscar a última linha depois.
def listar_produtos():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, preco, estoque FROM produtos"
    )
    linhas = cursor.fetchall()

    conexao.close()
    return linhas
def atualizar_estoque(produto_id, novo_estoque):
    conexao =  sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE produtos SET estoque = ? WHERE id = ?",
        (novo_estoque, produto_id)
    )

    conexao.commit()
    conexao.close()
    # Query parametrizada (com ?) em vez de concatenar string. Evita SQL Injection e trata os valores com segurança.
def inserir_item_carrinho(produto_id):
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor

    cursor.execute(
        "INSERT INTO carrinho (produto_id) VALUES (?)",
        (produto_id)
    )

    conexao.commit()
    conexao.close()
    # Query parametrizada (com ?) em vez de concatenar string. Evita SQL Injection e trata os valores com segurança.
def listar_itens_carrinho():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT produtos.id, produtos.nome, produtos.preco, produtos.estoque
        FROM carrinho
        JOIN produtos ON carrinho.produto_id = produtos.id
    """)
    linhas = cursor.fetchall()

    conexao.close()
    return linhas
def limpar_carrinho():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM carrinho"
    )

    conexao.commit()
    conexao.close()