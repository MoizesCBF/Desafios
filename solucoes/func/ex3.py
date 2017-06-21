'''
Idéia:

função recebe dois números(num_1 e num_2):
    SE, resto da divisão --> num_2/num_1=0:
        retorne verdade (True)
    SE NÃO:
        retorne falso (False)
'''

'Código'

#  ________________Funções_________________
def verificador(num1, num2):
    if ((num2%num1)==0):
        return True
    else:
        return False
#  _____________________________Fim funções


a = eval(input('Digite o 1º número: '))
b = eval(input('Digite o 2º número: '))

resposta = verificador(a, b)
print(resposta)

