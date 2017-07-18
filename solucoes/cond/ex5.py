
# Simulador de empréstimo bancário

salario = float(input('Salario: R$'))
imovel = float(input('Valor do imovel: R$'))
tempo = int(input('Tempo(anos) de financiamento: '))

tempo *= 12  # converte tempo em meses
mensalidade = imovel / tempo
limite = salario * .3

if mensalidade > limite:
    print('Empréstimo negado')

else:
    print('Empréstimo aprovado')
