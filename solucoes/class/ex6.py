# Creditos: Veronica

class Carro:
    def __init__(self, marca="Chevrolet", modelo="Camaro", ano="2017", cor='vermelho'):
        self.velocidade=0.0
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        self.comb=0.0
        
    def mostrar(self):
        print('\nMarca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Ano: ', self.ano)
        print('Cor:', self.cor)
        print('Velocidade:', self.velocidade)
        print('Combustivel: ', self.comb)
        print('')
        
    def abastecer(self,qtd):
        self.comb=self.comb+qtd
        if self.comb>80:
            print("Tanque cheio")
            self.comb=80
        print("Voce tem",self.comb," litros no tanque")

    def acelerar (self, quanto= 1.0):
        if self.comb > 0.2*quanto:
            if self.velocidade+ quanto <= 220:
                self.velocidade = self.velocidade + quanto
                print('Muito bom, agora sua velocidade atual é de: ', self.velocidade, "km/h")
                self.comb = self.comb - 0.2*quanto
            else:
                print("Por motivos de segurança, não vamos acelerar mais do que 220km/h. Sua velocidade ainda é: ", self.velocidade, "km/h")
        else:
            print('Voce precisa de combustivel!')
    def freiar (self, quanto= 1.0):
        if self.velocidade- quanto>=0:
            self.velocidade= self.velocidade-quanto
            print('Muito bom, agora sua velocidade atual é de: ', self.velocidade, "km/h")
        else:
            print("Não dá para ter uma velocidade negativa. Sua velocidade ainda é: ", self.velocidade, "km/h")
        


print('Olá, bem vindo ao teste drive do nosso carro, um Camaro vermelho. Siga as instruções a seguir para o melhor aproveitamento da experiencia')
carro=Carro()

while True:
    print("  M E N U")
    print("-----------")
    print("1. Acelerar")
    print("2. Freiar")
    print("3. Abastecer")
    print("4. Mostrar dados do carro")
    print("5. Sair do test-drive")
    
    opcao=input('Digite sua opcao: ')
    if opcao == "1" :
        quanto=int(input("Quanto deseja acelerar?"))
        carro.acelerar(quanto)
    elif opcao == "2" :
        quanto= int(input("Quanto deseja freiar?"))
        carro.freiar(quanto)
    elif opcao=="3":
        quanto=int(input("Quanto deseja abastecer?"))
        carro.abastecer(quanto)
    elif opcao == "4":
        carro.mostrar()
    elif opcao == "5":
        if carro.velocidade > 0:
            print('Voce precisa parar o carro completamente!')
        else:
            break


print("Agora que já testamos nosso carro, vamos montar o seu!")
print("Caso pule o modelo, será vinculado a que tinha nosso carro do teste drive (Chevrolet Camaro vermelho 2017)")

marca=input("Digite a marca do carro: ")
if marca=="":
    novoCarro = Carro()
else:
    modelo=input("Digite o modelo do carro: ")
    ano=input("Digite o ano do carro: ")
    cor=input("Digite a cor do carro: ")
    novoCarro = Carro(marca, modelo, ano, cor)
    
novoCarro.mostrar()








