'''
Idéia:

- Receber o numero inteiro
- Calcular se é divisivel por 2

SE resposta for par:
    imprime um texto dizendo que é par
SE NÃO:
    imprime um texto dizendo que é impar
'''

'Código:'

numero=eval(input("Digite um número: "))
resposta = numero%2

if resposta==0:
    print("Seu número é par!")
else:
    print("Seu número é impar!")

