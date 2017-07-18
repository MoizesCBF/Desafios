
# Escolha uma operação p/ exibir o resultado

num1 = float(input('Número 1:'))
num2 = float(input('Número 2:'))

menu = '''
    -------- MENU --------
    1. Para soma (+)
    2. Para subtração (-)
    3. Para multiplicação (*)
    4. Para divisão (/)
    
    Sua escolha: '''

escolha = input(menu)

if escolha == '1':
    print('{} + {} = {}'.format(num1, num2, (num1+num2)))

elif escolha == '2':
    print('{} - {} = {}'.format(num1, num2, (num1-num2)))

elif escolha == '3':
    print('{} * {} = {}'.format(num1, num2, (num1*num2)))

else:
    print('{} / {} = {}'.format(num1, num2, (num1/num2)))
