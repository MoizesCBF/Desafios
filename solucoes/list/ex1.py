'''________________Ideia____________________
- Pedir ao usuário duas listas;
- Devemos varrer ambas as listas e adicionar
cada elemento encontrado em uma nova varia-
vel do tipo lista;
- Mostrar na tela a nova lista gerada.
   ___________________________Fim da idea'''


#  ________________Código___________________

texto = '''Olá, digite duas listas. Iremos
retornar uma terceira lista com os elementos
da primeira e a segunda lista. \n'''
print(texto)

#  Primeira etapa
lista1 = (input('Digite a 1ª lista: '))
lista2 = (input('Digite a 2ª lista: '))
lista3 = [] # Lista vazia

'''Usaremos o For para ler ambas as listas
e adicionar seus elementos à lista3'''

#  Segunda etapa
for elemento in lista1:
    lista3.append(elemento)
'Adicione um separador entre lista 1 e 2'
lista3.append(' ') 
for elemento in lista2:
    lista3.append(elemento)

#  Terceira etapa
for elemento in lista3:
    print(elemento, end='')
#  ____________________________Fim do código
