'''
Idéia:

função recebe um número (num): quadrado 
recebe número ao quadrado retorna quadrado
'''

'Código:'

#  _________________Funções________________
def area(num):
    quadrado = num * num
    return quadrado
#  _____________________________Fim funções

print('Descubra o área de um quadrado.')
lado = int(input(
    'Digite um dos lados do quadrado: '))

resposta = area(lado)
texto = 'A área do quadrado vale {}'          
print(texto.format(resposta))
