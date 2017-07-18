
vel_atual = float(input('Velocidade atual: '))

if vel_atual > 80:
    print()
    print('Você foi multado!')
    print('{}km acima do tolerado.'.format(vel_atual-80))
    print('Total a pagar: R${:.2f}'.format((vel_atual-80)*5.0))
else:
    pass  # este comando não faz nada