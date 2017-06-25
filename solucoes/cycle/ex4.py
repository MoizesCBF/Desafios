'''________________Ideia____________________
Multiplcar um nº por outro nº usando apenas
operações de soma:

- Receber dois numeros do teclado;
- Criar um acumulador (valor inicial = 1);
- Criar variavel para guardar resposta;
- ENQUANTO acumulador for <= 1ºnº recebido:
      resposta += segundo nº
      aumente o valor de acumulador em 1
- Ao final do loop mostre na tela o valor de
  resposta.
   ___________________________Fim da idea'''


#  ________________Código___________________
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
acumulador = 1
resposta = 0
texto = "A multiplicação de {} por {} é:"
print(texto.format(num1, num2), end=' ')

while acumulador <= num1:
    resposta += num2
    acumulador += 1
print(resposta)
#  ____________________________Fim do código

