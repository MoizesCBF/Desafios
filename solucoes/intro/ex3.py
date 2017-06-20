'''
Idéia

Receber do usuário:
- Km percorrido;
- Tempo(dias) alugado;

Calcular total a pagar:
total = (km * 0.15)+(tempo * 60)
'''

'Código'

km = input('Digite km percorrido: ')
t = input('Digite tempo(dias) alugado: ')

#  Calcula-se total a pagar:
#  Tarifa1 = valor por km/rodado
#  Tarifa2 = valor por diária
tarifa1 = float(km) * .15
tarifa2 = float(t) * 60
total = tarifa1 + tarifa2

texto = 'Total a pagar R${:.2f}'
print(texto.format(total))
