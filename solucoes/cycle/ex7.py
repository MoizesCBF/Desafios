
# Simulador de rendimento na poupança

inicial = float(input('Valor inicial: R$'))
deposito = float(input('Deposito: R$'))
taxa = float(input('Rendimento a.a.: '))

taxa /= 12  # converte para taxa mensal
mes = 1
depositado = inicial
valor = inicial

while mes <= 24:
    print('{:0>2}º mês rendeu R${:.2f}'
        ''.format(mes, (valor*(taxa/100))))
    valor += valor*(taxa/100)
    valor += deposito
    depositado += deposito
    mes += 1

print()  # pula 1 linha

print('Total depositado: R${:.2f}'
      ''.format(depositado))
print('Total de rendimento: R${:.2f}'
      ''.format(valor-inicial))
print('Disponível na poupança: R${:.2f}'
      ''.format(valor))
