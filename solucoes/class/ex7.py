
from ex5 import ContaCorrente


class ContaEspecial(ContaCorrente):
    def __init__(self, nome, codigo, saldo, cheque):
        ContaCorrente.__init__(self, nome, codigo, saldo)
        self.__saldoespecial = cheque

    def get_saldoespecial(self):
        return self.__saldoespecial

    def saquespecial(self, valor):
        atual = self.get_saldo() + self.get_saldoespecial()
        if (atual - valor) >= 0:
            self.set_saldo(self.get_saldo()-valor)
        else:
            print('Saldo insuficiente')


usuario = ContaEspecial('Kamen', '000042', 300, 500)

while True:
    menu = input('''
        MENU
    
    1. Consultar saldo
    2. Sacar
    3. Depositar
    4. Encerrar
    
    Sua escolha: ''')

    while menu not in '1234':
        menu = input('Escolha inválida, tente novamente: ')

    if menu == '1':
        print()
        print('Cliente: {} \t Código: {}'.format(usuario.cliente, usuario.code))
        print('\nSaldo atual: \t\t R${:.2f}'.format(usuario.get_saldo()))
        print('Cheque Especial: \t R${:.2f}'.format(usuario.get_saldoespecial()))
        print('Saldo + limite: \t R${:.2f}'.format(usuario.get_saldoespecial()+usuario.get_saldo()))
        print()

    elif menu == '2':
        value = input('\nValor para saque: R$')
        usuario.saquespecial(float(value))

    elif menu == '3':
        value = input('\nValor para deposito: R$')
        usuario.deposito(float(value))

    else:
        break
