
entrada = input('Digite algo: ')
tamanho = len(entrada)
inverso = []  # lista vazia
igual = False

# cria lista inversa de entrada
for i in range(tamanho-1, -1, -1):
    inverso.append(entrada[i])

# compara entrada com seu inverso
for index, valor in enumerate(entrada):
    if valor == inverso[index]:
        igual = True
    else:
        igual = False
        break

if igual:
    texto = '{} é um palíndromo!'
    print(texto.format(entrada))
else:
    texto = '{} não é um palíndromo!'
    print(texto.format(entrada))
