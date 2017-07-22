
def meuGrep(nome_arq, alvo):
    arquivo = open(nome_arq, 'r')
    conteudo = arquivo.read()
    conteudo=conteudo.split('\n')
    tamanho = len(conteudo)

    for i in range(tamanho):
        if alvo in conteudo[i]:
            print(conteudo[i])
    arquivo.close()

meuGrep('ex8.txt', 'line')