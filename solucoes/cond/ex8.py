'''
Idéia:

SE condição1:
    imprimir texto...
SE NÃO:
    SE condição2:
        imprimir texto...
    SE NÃO:
        SE condição3:
            imprimir texto...
        SE NÃO:
            imprimir texto...
'''

'Código:'

peso=eval(input("Digite o seu peso(kg): "))
altura=eval(input("Digite a sua "
                            "altura(m): "))
IMC=peso/(altura*altura)

if IMC<18.5:
    print("Você está abaixo do peso")
else:
    if IMC>=18.5 and IMC<=24.9:
        print("Você está saudável!")
    elif IMC>=25 and IMC<=29.9:
        print("Você está acima do peso")
    elif IMC>=30 and IMC<=34.9:
        print("Obesidade I")
    elif IMC>=35 and IMC<=39.9:
        print("Obesidade II")
    else:
        print("Obesidade III")
    
print('terminou o programa')

