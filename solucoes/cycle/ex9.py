
soma = 0
qtd = 0

print('Digite um Nº ou 0 para sair')

while True:
    num = input('Numero: ')
    if num == '0':
        break
    else:
        qtd += 1
        soma += float(num)

print('Quantidade: {} números'.format(qtd))
print('A soma deles vale: {}'.format(soma))
print('A média vale: {}'.format(soma/qtd))
