'''________________Ideia____________________
- Receber um numero do teclado;
- Criar um acumulador (valor inicial = 1);
- ENQUANTO acumulador for <= nº recebido:
      Verifiva se o resto da divisao é zero
      SE acumulador for multiplo de 3:
          Mostre valor de acumulador
      SE NÃO:
          Não faça nada
      aumente o valor de acumulador em 1
   ___________________________Fim da idea'''


#  ________________Código___________________
referencia = input('Digite um numero: ')
acumulador = 1
texto = 'Múltiplos de 3 de 0 até {}: '
print(texto.format(referencia))

while acumulador <= int(referencia):
    if acumulador % 3 == 0:
        print(acumulador, end=' ')
    else:
        pass  # Não faz nada
    acumulador += 1
#  ____________________________Fim do código

