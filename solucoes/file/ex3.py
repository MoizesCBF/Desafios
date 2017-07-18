
impar = open('impares.txt', 'r')
par = open('pares.txt', 'r')

conteudo = []  # lista vazia

for numero in impar.readlines():
    aux = numero.split('\n')[0]
    conteudo.append(int(aux))

for numero in par.readlines():
    aux = numero.split('\n')[0]
    conteudo.append(int(aux))

# sorted --> organiza a lista (crescente)
print(sorted(conteudo))

impar.close()
par.close()
