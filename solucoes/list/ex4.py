
'''_________________Ideia__________________
- Receber uma expressão qualquer do teclado
- Contar quantos '(' existem na string
- Contar quantos ')' existem na string
- Se o nº de '(' for diferente de ')', diga
ao usuário que existem X parenteses que não
foram fechados.
_______________________________Fim ideia'''


#  ________________Código__________________
exp = input('Digite uma expressão: ')
abertos  = 0
fechados = 0

for char in exp:
    if char == '(':
        abertos += 1
    elif char == ')':
        fechados += 1
    else:
        pass  #  Este comando nâo faz nada

'Verifique se abertos é igual a fechados'
resp = abertos - fechados
if resp != 0:
    texto = 'Existem {} parenteses errados'
    if resp < 0:
        resp *= -1 #  Garante nº positivo
        print(texto.format(resp))
    else:
        print(texto.format(resp))
else:
    print('Todos parenteses fechados.')
#  ___________________________Fim do código
