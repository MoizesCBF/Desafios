
class Televisor:
    def __init__(self):
        self.__volume = 30
        self.__canal = 1
        self.__estado = 'off'

#   Metodos retornar Canal/Volume/Estado
    def get_canal(self):
        return self.__canal
    def get_volume(self):
        return self.__volume
    def get_estado(self):
        return self.__estado

#   Metodo alterar volume
    def set_volume(self, vol):
        self.__volume += vol
        

#   Metodo alterar canal
    def set_canal(self, chn):
        self.__canal += chn
        
#   Metodo ligar/desligar TV
    def power(self):
        if (self.__estado == 'on'):
            self.__estado = 'off'
        else:
            self.__estado = 'on'

#   Inicio do Programa:
tv = Televisor()

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
        escolha=input('\n Digitou um numero? Tente de novo: ')

    if (escolha=='1'):
        tv.power()
    elif (escolha == '6'):
        break
    if (tv.get_estado()=='off'):
        print('{:^25}'.format('TV desligada'))
    elif (escolha=='2'):
        tv.set_canal(1)
    elif (escolha=='3'):
        tv.set_canal(-1)
    elif (escolha=='4'):
        vol=int(input('Quanto gostaria de aumentar? (Atual %d)\n'\
                  %tv.get_volume()))
        if (vol<0):
            vol *= (-1)
        tv.set_volume(vol)
    elif (escolha=='5'):
        vol=int(input('Quanto gostaria de diminuir? (Atual %d)\n'\
              %tv.get_volume()))
        if (vol>0):
            vol *= (-1)
        tv.set_volume(vol)

    if (tv.get_estado()=='on'):
        print(' {:^40}\n'.format('TV SANGSUGA'))
        print(' Estado atual:', end='')
        print(' {:.>34}'.format(tv.get_estado()))
        print(' Canal:', end='')
        print(' {:.>40}'.format(tv.get_canal()))
        print(' Volume:', end='')
        print(' {:.>40}'.format(tv.get_volume()))

exit()