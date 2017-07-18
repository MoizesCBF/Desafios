
# Calculando preço da passagem

km = input('Distância da viagem: ')

if int(km) > 200:
    total = int(km) * .45

else:
    total = int(km) * .5

print('Valor da passagem: R${:.2f}'.format(total))
