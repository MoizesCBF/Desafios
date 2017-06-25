'''________________Ideia____________________
- Receber um numero do teclado;
- Criar um acumulador (valor inicial = 1);
- ENQUANTO acumulador for <= nº recebido:
      Verifiva se o resto da divisao é zero
      SE acumulador for par:
          Não faça nada
      SE NÃO:
          Mostre valor de acumulador

      aumente o valor de contador em 1
   ___________________________Fim da idea'''


#  ________________Código___________________
referencia = input('Digite um numero: ')
acumulador = 1
texto = 'Nºs ímpares de 0 até {}: '
print(texto.format(referencia))

while acumulador <= int(referencia):
    if acumulador % 2 == 0:
        pass #  Não faz nada
    else:
        print(acumulador, end=' ')
    acumulador += 1
#  ____________________________Fim do código

