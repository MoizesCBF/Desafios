'''_________________Ideia__________________
- Criar variáveis para guardar o maior e
menor valor e uma outra para média;
- Percorrer a lista T elemento por elemento
- Para cada elemento da lista T:
  some elemento à média
  SE elemento for menor que menor_valor:
      menor_valor = elemento
  SE elemento for maior que maior_valor:
      maior_valor = elemento
  SE NÃO:
      não faça nada
  média = média / nº de elementos em T
_______________________________Fim ideia'''


#  ________________Código__________________
menor = 0
maior = 0
media = 0
T = [-10, -8, 0, 1, 2, 5, -2, -4]

'Percorre lista T'
for temperatura in T:
    media += temperatura
    if temperatura < menor:
        menor = temperatura
    elif temperatura > maior:
        maior = temperatura
    else:
        pass #  este comando não faz nada
    media = media // len(T)

'Mostrar resultados na tela'
texto = 'Maior temperatura: {}\n' \
        'Menor temperatura: {}\n' \
        'Média de temperatura: {}'
print(texto.format(maior, menor, media))

#  ___________________________Fim de código
