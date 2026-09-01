# Loja Virtual (Python)

Projeto de loja virtual desenvolvido em Python, criado como parte do meu aprendizado como estudante de Análise e Desenvolvimento de Sistemas (ADS).

## Funcionalidades

- Listagem de produtos
- Adição de produtos ao carrinho
- Visualização do carrinho com total
- Finalização de compra
- Cadastro de novos produtos
- Persistência de dados em banco de dados SQLite

## Estrutura do projeto

- `Loja.py` - menu principal e fluxo de interação com o usuário
- `modelos.py` - classes `Produtos` e `Carrinho`
- `banco.py` - funções de acesso ao banco de dados (SQLite)

## Conceitos aplicados

- Programação Orientada a Objetos (classes 'Produto' e 'Carrinho')
- Tratamento de erros e validação de entrada do usuário
- Estruturas de repetição e condicionais
- Banco de dados relacional (SQLite): criação de tabelas, chave estrangeira, INSERT, SELECT, UPDATE, DELETE e JOIN
- Queries parametrizadas (proteção contra SQL Injection)
- Organização de código em módulos (separação e responsabilidades)

## Como executar

\'\'\'bash
python loja.py
\'\'\'

## Próximos passos

- Testes automatizados


