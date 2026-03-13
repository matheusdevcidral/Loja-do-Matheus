## Sobre o Projeto
Este projeto simula um sistema de gestão básico para pequenos negócios, operado inteiramente pelo terminal. O usuário pode cadastrar clientes com seus respectivos serviços e valores, registrar vendas e acompanhar o faturamento acumulado — tudo mantido em arquivos .txt.

## Funcionalidades

- Listagem de clientes cadastrados
- Cadastro de novos clientes com nome, serviço e valor
- Lançamento de faturamento (vendas e serviços)
- Visualização do faturamento total
- Validação de entradas com mensagens de erro
- Interface colorida no terminal com a biblioteca Rich

## Tecnologias Utilizadas

- Python 3
- Bibliotecas Rich e Time - a primeira para melhorar o visual e a segunda para melhor UX no terminal
- Arquivos .txt - persistência simples dos dados

## Para executar

1. Clone o repositório
git clone https://github.com/matheusdevcidral/Loja-do-Matheus.git

2. Instale a dependência
pip install rich

3. Execute
python sistema.py

## Aprendizados

- Manipulação de arquivos com open() (leitura e escrita)
- Validação robusta de entradas do usuário
- Formatação de strings com alinhamento (:<, :^, :>)
- Uso da biblioteca Rich para UI no terminal
- Organização de código com funções bem definidas
