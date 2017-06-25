
menu = '''\n\n
1 - Novo cliente
2 - Atender cliente
3 - Verificar quantos clientes na fila
4 - Sair
Sua escolha: '''
senha = 0
senhas = []  # Fila vazia

while True:
    opção = input(menu)

    #  _______________Opção 1______________
    if opção == '1':
        print('Aviso: Cliente adicionado.')
        senha += 1
        senhas.append(senha)
    #  _________________________Fim opção 1


    #  _______________Opção 2______________
    elif opção == '2':
        if len(senhas)!=0:
            print('Cliente atendido!')
            senhas.pop(0)
        else:
            print('Não há pessoas na fila')
    #  _________________________Fim opção 2


    #  _______________Opção 3______________
    elif opção == '3':
        if len(senhas)!=0:
            texto = 'Existem {} senhas:'
            print(texto.format(
                              len(senhas)))
            print('Senhas: ')
            for senha in senhas:
                print(senha, end=' ')
        else:
            print('Não há pessoas na fila')
    #  _________________________Fim opção 3


    #  _______________Opção 4______________
    elif opção == '4':
        print('Saindo...')
        break #  Este comando quebra o loop
    #  _________________________Fim opção 3


    #  __________Opção Inválida____________
    else:
        texto = '{} não é uma opção válida'
        print(texto.format(opção))
    #  __________________Fim opção invalida