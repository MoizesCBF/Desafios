# Solução proposta por @Yasmim#7532

leisQuant = int(input("Quantidade de leis"
                " para serem aprovadas:"))
todasLeis = []
for lei in range(leisQuant):
    leis = input("Digite a lei # "
                 "%d :" % (lei + 1))
    todasLeis.append(leis)

print("\nLISTA DE LEIS PARA APROVACAO\n")

for elem in todasLeis:
    print(elem)

leisFora = []
print("\n============================\n")
leisVotadas = int(input("Quantidade de "
      "leis votadas pela populacao para"
               " exclusao da votacao:"))

for item in range(leisVotadas):
    leiFora = input("Digite a lei"
                  " # %d :" % (item + 1))
    leisFora.append(leiFora)

print("\nLISTA DE LEIS PARA EXCLUSÃO DE"
      " VOTACAO\n")

for num in leisFora:
    print(num)

for i in todasLeis:
    for j in leisFora:
        if i == j:
            todasLeis.remove(j)

texto = "LISTA DE LEIS PARA VOTACAO FINAL:"
print("\n" + texto + "\n")
print("\n" + ('='*33) + "\n")
print(todasLeis)
