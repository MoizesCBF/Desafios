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
        if (isinstance(comida, Macaco)) :#  comida é mesma classe que macaco?
            if (self.__get_canibal()==True): #  Macaco é canibal ?
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
quantidade = 2 #   Inicio
while True:    
    escolha = input(intro) #   Menu de introdução
    while (escolha not in '123'):
        escolha = input('\tDigitou um numero? Tente novamente: ')
    if (escolha == '3'):
        print('\n\tSaindo do jogo...')
        exit()
    elif (escolha == '1'):
        quantidade = int(input("Quantidade de Macacos: "))
        while (quantidade <= 0):
            quantidade = int(input('Valor invalido. Teste de novo:'))
    else:
        monkeys = [] #   Criando macacos:
        for i in range(0, quantidade, 1):
            nome = input('\tNome do macaco%d: ' % (i + 1))
            chipanze = Macaco(nome)
            monkeys.append(chipanze)
        # Menu:
        while True:
            print('\nExistem %d macacos!' % (len(monkeys)))
            escolha = input(menu)
            while (escolha not in '123456'):
                escolha = input('Digitou um numero? Tente de novo: ')
            if (escolha == '6'):
                print('\n\tSaindo...')
                exit() # Sai do programa
            elif (escolha == '1'): # Alimenta macaco com fruta
                aux = input('Escolha (ex: 1 para o macaco 1): ')
                aux = int(aux)
                escolha = input(frutas)
                while(escolha not in '123'):
                    escolha=input('Erro. Tente de novo:')
                fruta = ['Banana', 'Morango', 'Abacaxi']
                if (escolha == '1'):
                    monkeys[(aux - 1)].comer(fruta[0])
                elif (escolha == '2'):
                    monkeys[(aux - 1)].comer(fruta[1])
                else:
                    monkeys[(aux - 1)].comer(fruta[2])
            elif (escolha == '2'): # Ver bucho
                aux = input('\tEscolha (ex: 2 para o macaco 2): ')
                aux = int(aux)
                bucho = monkeys[aux - 1].verBucho()
                print('Bucho macaco %d ''(%s): '%(aux, monkeys[aux-1].get_name()), end='')
                for i in bucho:
                    if (type(i) == Macaco):
                        print(i.get_name(), end=' ')
                    else:
                        print(i, end=' ')
                input()
            elif (escolha == '3'): # Digerir
                aux = input('Escolha (ex: 2 para o macaco 2): ')
                aux = int(aux)
                monkeys[aux - 1].digerir()
                print('\n\tDigestão '
                               'concluida!')
                input()
            elif (escolha == '5'): # Transforma macaco Canibal
                aux=input('Qual macaco? ')
                aux=int(aux)
                monkeys[aux-1].set_canibal()
            else: # Macaco canibal
                if (len(monkeys) == 1):
                    print('Sobrou apenas 1 macaco!')
                else:
                    aux = input('Macaco comedor: ')
                    aux2 = input('Macaco a ser comido: ')
                    aux  = int(aux)
                    aux2 = int(aux2)
                    macaco1=monkeys[aux-1]
                    macaco2=monkeys[aux2-1]
                    comeu = macaco1.comer(macaco2)
                    if (comeu == True):
                        monkeys.pop(aux2-1)
