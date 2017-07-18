
num1 = input('Numero 1: ')
num2 = input('Numero 2: ')
num3 = input('Numero 3: ')

# Verifica maior número
if num1 > num2:
    if num1 > num3:
        print('Maior número é:', num1)
    else:
        print('Maior número é:', num3)

elif num2 > num3:
    print('Maior número é:', num2)

else:
    print('Maior número é:', num3)

# Verifica menor número:
if num1 < num2:
    if num1 < num3:
        print('Menor número é:', num1)
    else:
        print('Menor número é:', num3)

elif num2 < num3:
    print('Menor número é:', num2)

else:
    print('Menor número é:', num3)