
dic = {}  # Dicionário vazio
frase = input('Digite uma string: ')

for letra in frase:
    if letra == ' ':
        pass
    elif letra not in dic:
        dic.setdefault(letra, 1)
    else:
        dic[letra] += 1

texto = '{:.<9}{}'
for letra in dic:
    print(texto.format(letra, dic[letra]))
