
# Simulador de rendimento na poupança

deposito = float(input('Depósito: R$'))
taxa = float(input('Rendimento a.a.: '))

taxa /= 12  # converte para taxa mensal
mes = 1
valor = deposito

while mes <= 24:
    print('{}º mês rendeu R${:.2f}'
        ''.format(mes, (valor*(taxa/100))))
    valor += valor*(taxa/100)
    mes += 1

print()  # pula 1 linha

print('Total depositado: R${:.2f}'
      ''.format(deposito))
print('Total de rendimento: R${:.2f}'
      ''.format(valor-deposito))
print('Disponível na poupança: R${:.2f}'
      ''.format(valor))
