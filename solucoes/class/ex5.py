
class ContaCorrente:
    def __init__(self, nome, codigo, saldo):
        self.cliente = nome   # publico
        self.code = codigo    # privado
        self.__saldo = saldo  # privado

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo = valor

    def saque(self, valor):
        atual = self.get_saldo()
        if (atual - valor) >= 0:
            self.set_saldo(atual-valor)
        else:
            print('Saldo insuficiente.')

    def deposito(self, valor):
        self.__saldo += valor
