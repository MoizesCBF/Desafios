#  ____________Funções_________________
def operadorLista(lista):
    quantidade = 0
    somatorio = 0
    for numero in lista:
        quantidade += 1
        somatorio += int(numero)
    media = somatorio / quantidade
    return quantidade, somatorio, media
#  _________________________Fim funções

texto1 = 'Digite uma lista de numeros separados por espaço'
lista = input(texto1)
lista = lista.split(' ')

quantidade, somatorio, media = operadorLista(lista)
texto2 = 'Quantidade: {}\nSomatorio: {}\nMedia: {}'
print(texto2.format(quantidade, somatorio, media))
