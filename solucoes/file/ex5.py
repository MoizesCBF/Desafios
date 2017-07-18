
# Digite 10 nomes e respecitvos telefones

agenda = open('ex5.txt', 'w')
dic = dict()  # Dicionario vazio

for contador in range(10):
    texto = '{}º nome: '
    nome = input(texto.format(contador+1))
    texto2 = 'Telefone de {}: '
    tel = input(texto2.format(nome))
    dic.setdefault(nome, tel)

for nome in sorted(dic):
    t = '{:.<20}{}'
    agenda.write(t.format(nome, dic[nome]))
    agenda.write('\n')

agenda.close()
