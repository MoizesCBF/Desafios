'''
Idéia:

função recebe dois números(num_1 e num_2):
    SE o resto da divisão de num_2 por num_1 for zero:
        retorne verdade (True)
    SE NÃO:
        retorne falso (False)
'''

'Código'

#  ________________Funções__________________
def verificador(num1, num2):
    if ((num2%num1)==0):
        return True
    else:
        return False
#  _______________________________Fim funções


a = eval(input('Digite o 1º número: '))
b = eval(input('Digite o 2º número: '))

resposta = verificador(a, b)
print(resposta)

         
