
inicio = input('Palavra secreta: ')
print('\n'*200)

palavra = [letra for letra in inicio]
segredo = ['_' for i in range(len(inicio))]
tentativas = 3
achou = False

menu = '''
***** MENU *****
1. Jogar
2. Ver resposta
3. Sair

Sua escolha: '''

while True:
    print('*'*5+' JOGO DA FORCA '+'*'*5)
    escolha = input(menu)

    while escolha not in '1 2 3':
        print('escolha inválida.')
        escolha = input('Tente de novo: ')

    if escolha == '1':
        texto = '\nVocê tem {} tentativas.\n'
        print(texto.format(tentativas))

        for letra in segredo:
            print(letra, end='')
        print('\n'*2)  # pula 2 linhas

        x = input('Tente uma letra: ')

        for index, char in enumerate(palavra):
            if char.upper() == x.upper():
                segredo[index] = x.upper()
                achou = True
            else:
                pass

        if not achou:
            tentativas -= 1
            t = '{} não existe no segredo.\n'
            print('\nVocẽ errou.')
            print(t.format(x))
        else:
            pass

    elif escolha == '2':
        txt = 'A palavra secreta é: {}'
        print(txt.format(inicio.upper()))

    else:
        break

    if tentativas == 0:
        print('\n\nGAME OVER')
