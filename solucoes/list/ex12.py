
def rol(lista):
    texto = '{:<10} {:<10} {:<10} {:^10}'
    print(texto.format('Último',
                       'Primeiro',
                       'Classe',
                       'Nota Média'))

    for i in range(len(lista)):
        aux = lista[i]
        for j in range(len(aux)):
            if j == len(aux)-1:
                txt = '{:^10.2f}'
                print(txt.format(aux[j]),
                      end=' ')
            else:
                t = '{:10}'
                print(t.format(aux[j]),
                      end=' ')
        print('')


dados =[['DeMoines', 'Jim', 'Pleno', 3.45],
        ['Pierre', 'Sophie', 'Pleno', 4.0],
      ['Columbus', 'Maria', 'Sênior', 2.5],
      ['Phoenix', 'River', 'Júnior', 2.45],
      ['Olympis', 'Edgar', 'Júnior', 3.99]]

rol(dados)
