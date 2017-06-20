'''
Ideia

Receber do usuario as informações:
- Distância a percorrer;
- Velocidade média esperada.

Calcular tempo de viagem:
Tempo = Distancia / Velocidade
'''

'Código'

d = input('Distância à percorrer(km): ')
v = input('Velocidade esperada(km/h): ')

#  Calcula-se o tempo:
t = float(d) / float(v)

texto = 'Tempo de viagem: {} horas.'
print(texto.format(int(t)))
