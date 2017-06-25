'''________________Ideia____________________
- Criar uma variavel contador (valor=10);
- ENQUANTO contador for maior ou igual à 0:
  mostre na tela o valor de contador
  subtraia o valor de contador em 1
  SE o valor de contador for igual a zero:
      mostre na tela 'FOGO !!!'
  SE NÃO:
      não faça nada
   ___________________________Fim da idea'''


#  ________________Código___________________
contador = 10
input('Pressione enter para começar:')
while contador >= 0:
    print(contador)
    input() #  aguarda tecla enter
    if contador == 0:
        print('FOGO !!!')
    else:
        pass #  este comando não faz nada
    contador -= 1
#  ____________________________Fim do código
