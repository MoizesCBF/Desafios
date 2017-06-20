'''
Idéia

Receber do usuário os seguintes dados:
- Valor da temperatura ºC

Converter para ºF:
ºF = ((9*ºC)/5)+32
'''

'Código'

c = input('Temperatura ºC: ')

#  Converter para ºF:
f = ((9*float(c))/5) + 32

texto = 'Nova temperatura: {}ºF'
print(texto.format(f))
      
