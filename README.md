# Loja Virtual (Python)

Projeto de loja virtual desenvolvido em Python, criado como parte do meu aprendizado como estudante de Análise e Desenvolvimento de Sistemas (ADS).

## Funcionalidades

- Sistema de login e criação de conta
- Controle de acesso (usuario admin x cliente)
- Listagem de produtos
- Adição de produtos ao carrinho
- Visualização do carrinho com total
- Finalização de compra
- Cadastro de novos produtos (admin)
- Edição de produtos existentes (admin)
- Persistência de dados em banco de dados SQLite

## Estrutura do projeto

- `loja.py` - menu principal e fluxo de interação com o usuário
- `modelos.py` - classes `Produto` e `Carrinho`
- `banco.py` - funções de acesso ao banco de dados (SQLite)

## Conceitos aplicados

- Programação Orientada a Objetos (classes 'Produto' e 'Carrinho')
- Tratamento de erros e validação de entrada do usuário
- Estruturas de repetição e condicionais
- Banco de dados relacional (SQLite): criação de tabelas, chave estrangeira, INSERT, SELECT, UPDATE, DELETE e JOIN
- Queries parametrizadas (proteção contra SQL Injection)
- Organização de código em módulos (separação e responsabilidades)
- Autenticação de usuário com hash de senha (hashlib) e validação de senha forte com expressões regulares (re)
- Controle de acesso ao perfil de usuário (admin x cliente)

## Instalação

\`\`\`bash
pip install -r requirements.text
\`\`\`

## Executando os testes

\`\`\`bash
python -m pytest
\`\`\`

## Como executar loja

\`\`\`bash
python loja.py
\`\`\`

## Próximos passos

- Interface web (Flask)


