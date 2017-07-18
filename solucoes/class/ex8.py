
class NumeroComplexo:
    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    #   Função que soma dois numeros complexos:
    def soma_complexo(self, num2):
        soma = []
        soma.append((self.real) + (num2.real))
        soma.append((self.imaginaria) + (num2.imaginaria))
        print('(%d, %di)' % (soma[0], soma[1]))

    #   Função que subtrai dois numeros complexos:
    def subtracao_complexo(self, num2):
        subtracao = []
        subtracao.append((self.real) - (num2.real))
        subtracao.append((self.imaginaria) - (num2.imaginaria))
        print('(%d, %di)' % (subtracao[0], subtracao[1]))

    #   Função que multiplica dois numeros complexos;
    def multiplicacao_complexo(self, num2):
        mult = []
        mult.append((self.real * num2.real) - (self.imaginaria * num2.imaginaria))
        mult.append((self.real * num2.imaginaria) + (self.imaginaria * num2.real))
        print('(%d, %di)' % (mult[0], mult[1]))
        return mult

    #   Função que calcula conjugado:
    def conjugado(self):
        conj = []
        conj.append(self.real)
        conj.append(self.imaginaria * (-1))
        print('(%d, %di)' % (conj[0], conj[1]))

    #   Função que faz a divisão entre dois numeros imaginarios:
    def divisao_complexo(self, num2):
        conj = NumeroComplexo(num2.real, (num2.imaginaria * (-1)))
        dividendo = self.multiplicacao_complexo(conj)
        denominador = num2.multiplicacao_complexo(conj)
        resultado = []
        resultado.append(float(dividendo[0] / denominador[0]))
        resultado.append(float(dividendo[1] / denominador[0]))
        print('Divisão = (%.2f, %.2fi)' % (resultado[0], resultado[1]))


# Função que lê parte real e imaginaria a partir do teclado:
def leitura():
    real = float(input('Parte Real:'))
    img = float(input('Parte Imaginaria:'))
    return real, img


#   Iniciando Programa:
print('\nNumero Complexo 1\n')
real, img = leitura()
A = NumeroComplexo(real, img)

print('\nNumero Complexo 2\n')
real, img = leitura()
B = NumeroComplexo(real, img)

print('\nSoma entre (%d, %di) e (%d, %di) = ' \
      % (A.real, A.imaginaria, B.real, B.imaginaria), end='')
A.soma_complexo(B)

print('\nSubtração entre (%d, %di) e (%d, %di) = ' \
      % (A.real, A.imaginaria, B.real, B.imaginaria), end='')
A.subtracao_complexo(B)

print('\nMultiplicação entre (%d, %di) e (%d, %di) = ' \
      % (A.real, A.imaginaria, B.real, B.imaginaria), end='')
A.multiplicacao_complexo(B)

print('\nConjugado de (%d, %di) = ' % (A.real, A.imaginaria), end='')
A.conjugado()
print('Conjugado de (%d, %di) = ' % (B.real, B.imaginaria), end='')
B.conjugado()

print('\nDivisão de (%d, %di) por (%d, %di): ' \
      % (A.real, A.imaginaria, B.real, B.imaginaria))
A.divisao_complexo(B)

exit()
