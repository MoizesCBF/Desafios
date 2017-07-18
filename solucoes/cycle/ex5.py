'''________________Ideia____________________
Dividir um nº por outro nº usando apenas
operações de subtração:

- Receber dois numeros do teclado;
- Criar variavel para guardar resposta;
- ENQUANTO num1 - num2 for maior que zero:
      primeiro nº -= segundo nº
      aumente o valor de resposta em 1
- Ao final do loop mostre na tela o valor de
  resposta.
   ___________________________Fim da idea'''


#  ________________Código___________________
num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))
resposta = 0
texto = "A divisão inteira de {} por {} é"
print(texto.format(num1, num2), end=' ')

while (num1 - num2) >= 0:
    num1 -= num2
    resposta += 1

print(resposta)
#  ____________________________Fim do código

