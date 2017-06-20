'''
Idéia

Função recebe dois números (base e altura):
    area recebe cálculo da area do triângulo
    retorna area
'''

'Código'

#  ________________Funções_______________
def area(base, altura):
    area = (base*altura)/2
    return area
#  ___________________________Fim funções

print('Descubra a área do triângulo')

b = eval(input('Digite a base: '))
a = eval(input('Digite a altura: '))

resposta = area(b,a)
texto = 'A area do triângulo vale {}.'
print(texto.format(resposta))
