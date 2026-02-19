import json

def carregar_produtos(): #carrega os produtos salvos na lista
    try:
        with open('produtos.json', 'r') as f:
            return json.load(f)
    except:
        return []


def salvar_produtos(produtos): #salva os produtos na lista
    with open('produtos.json', 'w') as f:
        json.dump(produtos, f)


def titulo(): #titulo do programa
    print('=' * 26)
    print('  LOJA DO MATHEUS')
    print('=' * 26)


def menu(produtos): #menu interativo
    while True:
        print("""1 - Cadastrar produtos
2 - Exibir produtos
3 - Produto mais caro
4 - Menor estoque
5 - Valor total em estoque
6 - Sair""")
        opcao = int(input('\nEscolha sua opção: '))
        if opcao == 1:
            print()
            produtos = cadastrar_produtos(produtos)
            salvar_produtos(produtos)
            print()
        elif opcao == 2:
            print()
            exibir_produtos(produtos)
            print()
        elif opcao == 3:
            print()
            mais_caro = produto_mais_caro(produtos)
            print(f'\nO produto mais caro é {mais_caro['nome']} - R$ {mais_caro['preco']:.2f}')
        elif opcao == 4:
            print()
            menor = menor_estoque(produtos)
            print(f'\nMenor estoque: {menor['nome']} - {menor['quantidade']} unidades')
        elif opcao == 5:
            print()
            total = valor_total_estoque(produtos)
            print(f'\nValor total em estoque: R$ {total:.2f}')
        elif opcao == 6:
            sair()
            break
        else:
            print('\nOpção Inválida!')


def cadastrar_produtos(produtos): #1
    while True:
        produto = dict()
        produto['nome'] = input('Digite o nome do produto: ')
        produto['preco'] = float(input('Digite o preço do produto: '))
        produto['quantidade'] = int(input('Digite a quantidade do produto: '))
        produtos.append(produto)

        continuar = input('Deseja continuar? [S/N] ').strip().lower()[0]
        if continuar == 'n':
            break

    return produtos


def exibir_produtos(produtos): #2
    for p in produtos:
        print(f'Nome: {p['nome']} | Preço: {p['preco']:.2f} | Estoque: {p['quantidade']}')


def produto_mais_caro(produtos): #3
    mais_caro = max(produtos, key=lambda p: p['preco'])
    return mais_caro


def menor_estoque(produtos): #4
    menos_estoque = min(produtos, key=lambda p: p['quantidade'])
    return menos_estoque


def valor_total_estoque(produtos): #5
    valor_total = sum(p['preco'] * p['quantidade'] for p in produtos)
    return valor_total


def sair(): #6
    print('Finalizando o sistema...')
    print('Até logo!')


#Programa Principal
titulo()
produtos = carregar_produtos()
menu(produtos)
