# Proposto por @Schnnaps#8499

def bubblesort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j+1],lista[j] = \
                    lista[j],lista[j+1]
    print(lista)

bubblesort([3, 1, 7, 4, 9, 2, 5])