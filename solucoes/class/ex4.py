
from ex3 import Televisor


sangsuga = Televisor()

while True:
    escolha = input('''
        MENU

 1. Liga/desliga TV (@)
 2. Botao para cima (+)
 3. Botao para baixo(-)
 4. Aumentar volume (>)
 5. Diminuir volume (<)
 6. Encerrar simulador
''')
    while (escolha not in '123456'):
        escolha = input('\n Digitou um numero? Tente de novo: ')

    if (escolha == '1'):
        sangsuga.power()

    elif (escolha == '6'):
        break
    if (sangsuga.get_estado() == 'off'):
        print('{:^25}'.format('TV desligada'))

    elif (escolha == '2'):
        sangsuga.set_canal(1)

    elif (escolha == '3'):
        sangsuga.set_canal(-1)

    elif (escolha == '4'):
        vol=int(input('Quanto gostaria de aumentar? (Atual %d)\n' % sangsuga.get_volume()))

        if (vol<0):
            vol *= (-1)
        sangsuga.set_volume(vol)

    elif (escolha == '5'):
        vol=int(input('Quanto gostaria de diminuir? (Atual %d)\n' % sangsuga.get_volume()))

        if (vol>0):
            vol *= (-1)
        sangsuga.set_volume(vol)

    if (sangsuga.get_estado()=='on'):
        print(' {:^40}\n'.format('TV SANGSUGA'))
        print(' Estado atual:', end='')
        print(' {:.>34}'.format(sangsuga.get_estado()))
        print(' Canal:', end='')
        print(' {:.>40}'.format(sangsuga.get_canal()))
        print(' Volume:', end='')
        print(' {:.>40}'.format(sangsuga.get_volume()))

exit()
