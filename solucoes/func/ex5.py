#  ________________Funções_________________
def fatorial(num):
    aux = num - 1
    while (aux > 0):
        num = num * aux
        aux = aux - 1
    return num
#  ____________________________Fim funções

print('Descubra o fatorial de um número')
n = int(input('Digite um número: '))

resposta = fatorial(n)
texto = 'O fatorial de {} vale {}.'

print(texto.format(n, resposta))
