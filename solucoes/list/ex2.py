'''________________ideia___________________
- Receber lista 1 do usuário;
- Receber lista 2 do usuário;
- Criar nova lista a partir de lista 1 e 2

  SE o novo_elemento não estiver já contido
  na sua lista:
     Adicione novo_elemento à lista
  SE NÃO:
     Não faça nada
____________________________Fim de ideia'''

#  1ª etapa: Receber listas
lista1 = input('Elementos da 1ª lista: ')
lista2 = input('Elementos da 2ª lista: ')
lista3 = [] #  Lista vazia

#  2ª etapa: Adicionar elementos da lista1
#  e lista 2 em lista3
for elemento in lista1.split():
    if elemento not in lista3:
        lista3.append(elemento)
    else:
        pass #  não faz nada

for elemento in lista2.split():
    if elemento not in lista3:
        lista3.append(elemento)
    else:
        pass #  não faz nada

#  3ª etapa: Mostrar lista3 na tela
for elemento in lista3:
    print(elemento, end=' ')
print(lista3)