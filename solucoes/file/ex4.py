
# Este programa recebe um arquivo de texto
# "ex4.txt" que contém nomes de frutas

texto = open('ex4.txt', 'r')
dic = {}  # dicionário vazio
lista = []  # lista vazia

for linha in texto.readlines():
    lista.append(linha.split('\n'))

for linha in lista:
    for fruta in linha[0].split(' '):
        if fruta == ' ' or fruta == '':
            pass
        elif fruta not in dic:
            dic.setdefault(fruta, 1)
        else:
            dic[fruta] += 1

print()  # pula 1 linha
print('****** Contador de palavras ******')
print()  # pula 1 linha

# Imprimindo chaves e valores
for chave in dic:
    aux = '{:.<15}{}'
    print(aux.format(chave, dic[chave]))

texto.close()
