#  ________________Funções_________________
def operador(lista):
    quantidade = 0
    somatorio = 0
    for numero in lista:
        quantidade += 1
        somatorio += int(numero)
    media = somatorio / quantidade
    return quantidade, somatorio, media
#  _____________________________Fim funções

texto1 = 'Digite uma lista de números ' \
         '(separados por espaço): '
lista = input(texto1)
lista = lista.split(' ')

quant, somatorio, media = operador(lista)
texto2 = 'Quantidade: {}\nSomatorio: {}' \
         '\nMedia: {}'
print(texto2.format(quant, somatorio,
                                    media))
