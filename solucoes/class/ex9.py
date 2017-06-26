#teste
class Macaco:
    def __init__(self, nome):
        self.__bucho = []
        self.__name = nome
        self.__canibal = False

    def verBucho(self):
        bucho = []
        for i in self.__bucho:
            bucho.append(i)
        return bucho

    def comer(self, comida):
        #  comida é mesma classe que macaco?
        if (isinstance(comida, Macaco)):
            #  Macaco é canibal ?
            if (self.__get_canibal()==True):
                self.__bucho.append(comida)
                return True
        else:
            self.__bucho.append(comida)
            return True
        return False

    def digerir(self):
        self.__bucho = []

    def get_name(self):
        return self.__name

    def set_canibal(self):
        self.__canibal = True

    def __get_canibal(self):
        return self.__canibal


intro = '''
              ALIMENTE O MACACO
    ----------------------------------------
    1. Alterar quantidade de macacos (min 2)
    2. Iniciar Jogo
    3. Sair
\t'''
menu = '''
                    MENU
    ----------------------------------------
    1. Alimentar o macaco com fruta
    2. Ver bucho (estomago)
    3. Digerir
    4. Macaco canibal
    5. Make Monkey Canibal
    6. Sair
\t'''
frutas = '''
               ESCOLHA UMA FRUTA
    ----------------------------------------
    1. Banana
    2. Morango
    3. Abacaxi
\t'''

#   Inicio
quantidade = 2
while True:

    #   Menu de introdução
    escolha = input(intro)
    while (escolha not in '123'):
        escolha = input('\tDigitou um '
                'numero? Tente novamente: ')
    if (escolha == '3'):
        print('\n\tSaindo do jogo...')
        exit()
    elif (escolha == '1'):
        quantidade = int(input("\t"
                 "Quantidade de Macacos: "))
        while (quantidade <= 0):
            quantidade = int(input('\tValor'
               ' invalido. Teste de novo:'))
    else:
        #   Criando macacos:
        monkeys = []
        for i in range(0, quantidade, 1):
            nome = input('\tNome do macaco '
                           '%d: ' % (i + 1))
            chipanze = Macaco(nome)
            monkeys.append(chipanze)

        # Menu:
        while True:
            print('\n\tExistem %d macacos!'\
                           % (len(monkeys)))
            escolha = input(menu)
            while (escolha not in '123456'):
                escolha = input('\tDigitou '
               'um numero? Tente de novo: ')

            # Sai do programa
            if (escolha == '6'):
                print('\n\tSaindo...')
                exit()

            # Alimenta macaco com fruta
            elif (escolha == '1'):
                aux = input('\tEscolha (ex:'
                    ' 1 para o macaco 1): ')
                aux = int(aux)
                escolha = input(frutas)
                while(escolha not in '123'):
                    escolha=input('\tErro.'
                          ' Tente de novo:')
                fruta = ['Banana',
                         'Morango',
                         'Abacaxi']
                if (escolha == '1'):
                    monkeys[
                  (aux - 1)].comer(fruta[0])
                elif (escolha == '2'):
                    monkeys[
                  (aux - 1)].comer(fruta[1])
                else:
                    monkeys[
                  (aux - 1)].comer(fruta[2])

            # Ver bucho
            elif (escolha == '2'):
                aux = input('\tEscolha (ex:'
                    ' 2 para o macaco 2): ')
                aux = int(aux)
                bucho = monkeys[ 
                         aux - 1].verBucho()
                print('\tBucho macaco %d '
                      '(%s): '%(aux,
                monkeys[aux-1].get_name()),
                                     end='')

                for i in bucho:
                    if (type(i) == Macaco):
                        print(i.get_name(),
                                   end=' ')
                    else:
                        print(i, end=' ')
                input()

            # Digerir
            elif (escolha == '3'):
                aux = input('\tEscolha (ex:'
                    ' 2 para o macaco 2): ')
                aux = int(aux)
                monkeys[aux - 1].digerir()
                print('\n\tDigestão '
                               'concluida!')
                input()

            # Transforma macaco Canibal
            elif (escolha == '5'):
                aux=input('\tQual macaco? ')
                aux=int(aux)
                monkeys[aux-1].set_canibal()

            # Macaco canibal
            else:
                if (len(monkeys) == 1):
                    print('\tSobrou apenas '
                                '1 macaco!')
                else:
                    aux = input('\tMacaco '
                                'comedor: ')
                    aux2 = input('\tMacaco '
                           'a ser comido: ')
                    aux  = int(aux)
                    aux2 = int(aux2)
                    macaco1=monkeys[aux-1]
                    macaco2=monkeys[aux2-1]
                    comeu = \
                      macaco1.comer(macaco2)
                    'Verifica se comeu'
                    if (comeu == True):
                        monkeys.pop(aux2-1)
