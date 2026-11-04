# Coffee Shops Tia Rosa


#classe para clientes
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


#cardápio já pronto com as opções para simplificar o sistema
cardapio = [
    {'nome': 'Café Artesanal', 'ingredientes': 'Café Artesanal e Água', 'preco': 9.00},
    {'nome': 'Café Tradicional', 'ingredientes': 'Café Tradicional e Água', 'preco': 8.00},
    {'nome': 'Água', 'ingredientes': 'Água', 'preco': 5.00},
    {'nome': 'Suco', 'ingredientes': 'Suco e Água', 'preco': 7.00},
    {'nome': 'Pão de Queijo', 'ingredientes': 'Pão de Queijo', 'preco': 5.00},
    {'nome': 'Pão na Chapa', 'ingredientes': 'Pão com Manteiga', 'preco': 7.00},
    {'nome': 'Salgado', 'ingredientes': 'Salgado', 'preco': 8.00},
    {'nome': 'Pão com Ovo', 'ingredientes': 'Pão com Ovo', 'preco': 9.00}
            ]


#funcao que exibe o cardapio
def exibir_cardapio():
    print('\n\n           CARDÁPIO           ')

    for i in range(len(cardapio)):
        item = cardapio[i]

        print(i + 1, '-', item['nome'])
        print('Ingredientes:', item['ingredientes'])
        print('Preço: R$ {:.2f}'.format(item['preco']), '\n')


#variaveis para as listas
pedidos = []
clientes = []


# Início do menu em loop enquanto não for utilizado o break
while True:

    print('\n\n\t\t\t\t BEM VINDO(A) AO COFFEE SHOPS TIA ROSA!\n')
    print('1 - EXIBIR CARDÁPIO - REALIZAR PEDIDO')
    print('2 - VERIFICAR PEDIDOS')
    print('3 - CADASTRAR CLIENTES')
    print('4 - VENDAS DIÁRIAS')
    print('0 - ENCERRAR PROGRAMA')

    opcao = input('\n    DIGITE O NÚMERO DE ACORDO COM A OPÇÃO: ')
# finaliza o sistema caso utilizado opçao 0
    if opcao == '0':
        print('\n\nVOLTE SEMPRE E OBRIGADO PELA VISITA')
        break

    elif opcao == '1':

#funcao cardapio
        exibir_cardapio()

        numero = int(input('INFORME O NÚMERO DO PRODUTO ESCOLHIDO: '))
#inicio contagem dos itens do cardapio
        if numero < 1 or numero > len(cardapio):
            print('\nPRODUTO INVÁLIDO!')

        else:
            produto = cardapio[numero - 1]

            quantidade = int(input('DIGITE A QUANTIDADE: '))

            total = produto['preco'] * quantidade

            pedido = {
                'produto': produto['nome'],
                'quantidade': quantidade,
                'total': total
            }

            pedidos.append(pedido)

            print('\nPEDIDO REALIZADO COM SUCESSO!')
            print('Produto:', produto['nome'])
            print('Quantidade:', quantidade)
            print('Total: R$ {:.2f}'.format(total))

# menu exibindo item a item que o cliente escolheu
    elif opcao == '2':

        print('\n\n           PEDIDOS REALIZADOS           ')
# quantidade de pedidos realizados pelo cliente
        if len(pedidos) == 0:
            print('NENHUM PEDIDO REALIZADO.')

        else:
            for i in range(len(pedidos)):

                pedido = pedidos[i]

                print('\nPedido', i + 1)
                print('Produto:', pedido['produto'])
                print('Quantidade:', pedido['quantidade'])
                print('Total: R$ {:.2f}'.format(pedido['total']))

# cadastro feito a partir do nome e cpf do cliente
    elif opcao == '3':

        print('\n\n           CADASTRO DE CLIENTE           ')

        nome = input('INFORME O NOME DO CLIENTE: ')
        cpf = input('INFORME O CPF DO CLIENTE: ')

        # Criação de um objeto da classe Cliente
        cliente = Cliente(nome, cpf)

        clientes.append(cliente)

        print('\nCLIENTE CADASTRADO COM SUCESSO!')

# valor total das vendas do dia
    elif opcao == '4':

        print('\n           VENDAS DIÁRIAS           \n')

        total_vendas = 0

        for pedido in pedidos:
            total_vendas += pedido['total']

        print('TOTAL DE VENDAS: R$ {:.2f}'.format(total_vendas))

# caso digitado uma opçao diferente do exibido no menu
    else:
        print('\nOPÇÃO INVÁLIDA! ESCOLHA UMA OPÇÃO NO MENU!')