'''
Idéia:

função recebe dois números(num_1 e num_2):
    SE num_1 for maior que num_2:
        retorna num_1
    SE NÃO:
        retorna num_2
'''

'Código'

#  _________________Funções_________________
def retorna_maior(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2
#  ___________________________Fim de funções


print('Qual número é maior?')

num_1 = eval(input('Digite o 1º número: '))
num_2 = eval(input('Digite o 2º número: '))
resposta = retorna_maior(num_1, num_2)

texto = 'O maior número é {}!'
print(texto.format(resposta))


