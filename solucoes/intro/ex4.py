'''
Ideia

Receber do usuario as seguintes informações:
- Quantidade de cigarros fumados p/ dia;
- Tempo(anos) como fumante.

Calcular estimativa de vida:

-Quantidade de cigarros fumados p/ ano:
 quantidade p/ ano=(quantidade p/ dia)*365
 
-Quantidade de cigarrafos fumados(total):
 total = quantidade p/ ano * tempo(ano)

-Tempo perdido por cigarro:
 tempo(min) = quantidade p/ ano * 10

-Converter tempo(min) em tempo(dia):
 tempo = tempo(min) / 1440

OBS: 1 dia = 24 horas = 1440 minutos
 '''

'Código'

cigarret = input('Nº de cigarros '
                 'fumados p/ dia: ')
anos = input('Tempo como fumante: ')

#  Calcula-se nº cigarros fumados:
total = int(anos) * 365 * int(cigarret)

#  Calcula-se o tempo perdido em minutos:
tempo_min = total * 10

#  Converte-se tempo(min) em tempo(dia):
tempo_dia = int(tempo_min / 1440)

texto = 'Estima-se que você perdeu {}' \
                           ' dias de vida.'
print(texto.format(tempo_dia))

