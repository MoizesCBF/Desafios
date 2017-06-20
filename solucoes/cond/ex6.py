
'''
Idéia:

SE minutos for menor que 200:
    calcule o preço usando 0.2

SE NÃO:
    SE minutos for entre 200 e 400:
        calcule preço usando 0.18

    SE NÃO:
        calcule preço usando 0.15
'''

'Código:'

minutos=eval(input("Quantos minutos você usou esse mês: "))
if minutos<200:
    fatura=(minutos*0.2)
else:
    if minutos>=200 and minutos<=400:
        fatura=(minutos*0.18)
    else:
        fatura=(minutos*0.15)
print('Total a pagar: R${:.2f}'.format(fatura))


