
produto = dict()  # Dicionario vazio

menu = '''
******* MENU *******

1. Cadastrar produto
2. Exibir produtos
3. Sair'''

while True:
    print(menu)
    escolha = input('Sua escolha: ')

    while escolha not in '1 2 3':
        print('Escolha inválida.')
        escolha=input('Tente novamente: ')

    if escolha == '1':
        nome = input("Produto: ")
        preco = input('Preço: ')
        produto.setdefault(nome, preco)

    elif escolha == '2':
        t = '{:.<20}{}'
        for x in produto:
            print(t.format(x, produto[x]))

    else:
        break

