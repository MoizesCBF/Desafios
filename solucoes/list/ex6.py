'''_________________Ideia__________________
- Receber uma lista do usuário
- Ordenar usando método de ordenação de bo-
  lhas (bubble  sort)
_______________________________Fim ideia'''


#  ________________Código__________________

#  1ª etapa: Receber dados
lista = input('Digite os valores'
              ' separados por espaço: ')
lista = lista.split(' ')

'Convertendo lista em numeros inteiros'
for e, elemento in enumerate(lista):
    lista[e] = int(elemento)


#  2ª etapa: Aplicando método bubble sort
tamanho = len(lista)

while tamanho > 1:
    trocou = False
    indice = 0

    while indice < (tamanho-1):
        if lista[indice]>lista[indice+1]:
            trocou = True
            auxiliar = lista[indice]
            lista[indice] = lista[indice+1]
            lista[indice+1] = auxiliar
        indice += 1
    if not trocou:
        break
    tamanho -= 1


#  3ª etapa: Mostrar resultado na tela
decrescente = []
print('Ordem crescente:', end=' ')
for elemento in lista:
    print(elemento, end=' ')
    decrescente.insert(0, elemento)

print('\nOrdem decrescente: ', end='')
for elemento in decrescente:
    print(elemento, end=' ')


