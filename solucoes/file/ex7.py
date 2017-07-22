
def stringcount(nome_arquivo, alvo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read()
    ocorrencias = conteudo.count(alvo)
    arquivo.close()
    return ocorrencias

nome = 'example.txt'
quantidade = stringcount(nome, 'line')
print(quantidade)
